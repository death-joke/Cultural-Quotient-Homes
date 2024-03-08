import json
import math
from tqdm.auto import tqdm
from schools.main import parse_data_schools
from museums.museums import parse_data_museums
from dvf.get_dvf import parse_data_dvf
from cultural.parsers import parse_cultural_data


# create an output json file with the following structure:
# {
#     [
#         {
#             "code Insee": 22385,
#             "Commune": "Plouha",
#             "Nombre d'établissements scolaures": 3,
#             "Nombre de musées": 1,
#             "Nombre de bibliotheques": 1,
#             "Nombre de cinemas": 1,
#             "Nombre de monuments": 1,
#             "Valeur foncière moyenne": 200000
#         },
#         ...
#     ]
# }
data = []
schools = parse_data_schools()
print("🚀 schools parsed")
museums = parse_data_museums()
print("🚀 museums parsed")
dvf = parse_data_dvf()
print("🚀 dvf parsed")
bibli, cine, monuments = parse_cultural_data()
print("🚀 cultural parsed")

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
with open('out.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

