import json
import math
import geojson
import pandas as pd
from tqdm.auto import tqdm
from schools.main import parse_data_schools
from museums.museums import parse_data_museums
from dvf.get_dvf import parse_data_dvf
from cultural.parsers import parse_cultural_data
from geo_json.geo_json import parse_geojson



data = []
schools = parse_data_schools()
print("🚀 schools parsed")
museums = parse_data_museums()
print("🚀 museums parsed")
dvf = parse_data_dvf()
print("🚀 dvf parsed")
bibli, cine, monuments = parse_cultural_data()
print("🚀 cultural parsed")
geodata = parse_geojson()
print("🚀 geoJSON parsed")

for _, city in tqdm(dvf.iterrows(), total=len(dvf)):
    nb_schools = schools[schools['code_commune'] == city['Code INSEE']].shape[0] # OK
    nb_museums = museums[(museums['Commune'] == city['Commune']) & (museums['Code Postal'] == city['Code postal'])].shape[0] # OK
    try:
        nb_bibli = bibli[bibli['code_insee_commune'] == int(city['Code INSEE'])].shape[0]  # OK
        # Ne fonctionne pas avec la corse (2A et 2B) car les codes insee sont des strings et son mis null dans le jeu de donnée de Lina (faute de la source)
    except:
        nb_bibli = "N/A"
    
    nb_cine = cine[cine['code_insee'] == city['Code INSEE']].shape[0] # OK
    nb_monuments = monuments[monuments['code_insee_commune'].apply(lambda x : str(x)) == str(city['Code INSEE'])].shape[0] # OK


    # check if city['Valeur fonciere'] is a number
    if math.isnan(city['Valeur fonciere']):
        city['Valeur fonciere'] = "N/A"

    data.append({
        "code Insee": str(city['Code INSEE']),
        "Commune": city['Commune'],
        "Code postal": str(city['Code postal']),
        "Nombre d'établissements scolaires": nb_schools,
        "Nombre de musées": nb_museums,
        "Nombre de bibliotheques": nb_bibli,
        "Nombre de cinemas": nb_cine,
        "Nombre de monuments": nb_monuments,
        "Valeur foncière moyenne": city['Valeur fonciere']
    })



#transfor the data in a dataframe
data = pd.DataFrame(data)
data['transformed_code'] = data['code Insee'].apply(lambda x: x[:3] + '0' + x[3:] if x.startswith('97') else x)

for feature in geodata['features']:
    code_insee = feature['properties']['code']
    # get the row from the data file that has the same code_insee
    if code_insee == "75056":
        #make the sum of the value of the 20 arrondissements with code Insee from 75101 to 75120
        row = data[(data['code Insee'] >= '75101') & (data['code Insee'] <= '75120')].sum()
        ##make the mean  for the valeur foncière moyenne
        row['Valeur foncière moyenne'] = data[(data['code Insee'] >= '75101') & (data['code Insee'] <= '75120')]['Valeur foncière moyenne'].mean()
        #put the value Paris for the column Commune
        row['Commune'] = "Paris"
        #put the value 75056 for the column code Insee
        row['code Insee'] = "75056"
        row = pd.DataFrame([row])

        print(row)
    elif code_insee.startswith("97"):
        row = data[data['transformed_code'] == code_insee]    
    else :
        row = data[data['code Insee'] == code_insee]
        if code_insee == "01001":
            print(row)
    # if the row exists, add the properties to the feature
    if not row.empty:
        feature['properties']['Nombre d\'établissements scolaires'] = str(row['Nombre d\'établissements scolaires'].values[0])
        feature['properties']['Nombre de musées'] = str(row['Nombre de musées'].values[0])
        feature['properties']['Nombre de bibliotheques'] = str(row['Nombre de bibliotheques'].values[0])
        feature['properties']['Nombre de cinemas'] = str(row['Nombre de cinemas'].values[0])
        feature['properties']['Nombre de monuments'] = str(row['Nombre de monuments'].values[0])
        feature['properties']['Valeur foncière moyenne'] = str(row['Valeur foncière moyenne'].values[0])


#create a new geojson file with the modified properties
with open('result.geojson', 'w', encoding='utf-8') as outfile:
    geojson.dump(geodata, outfile, ensure_ascii=False)