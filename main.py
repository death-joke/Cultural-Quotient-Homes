import json
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
    if city['Code INSEE'] != "33063":
        continue
    nb_schools = schools[schools['code_commune'] == city['Code INSEE']].shape[0] # OK
    nb_museums = museums[(museums['Commune'] == city['Commune']) & (museums['Code Postal'] == city['Code postal'])].shape[0] # OK
    nb_bibli = bibli[bibli['code_insee_commune'] == int(city['Code INSEE'])].shape[0]  # OK
    nb_cine = cine[cine['code_insee'] == city['Code INSEE']].shape[0] # OK
    nb_monuments = monuments[monuments['code_insee_commune'] == int(city['Code INSEE'])].shape[0] # OK

    data.append({
        "code Insee": int(city['Code INSEE']),
        "Commune": city['Commune'],
        "Code postal": int(city['Code postal']),
        "Nombre d'établissements scolaires": nb_schools,
        "Nombre de musées": nb_museums,
        "Nombre de bibliotheques": nb_bibli,
        "Nombre de cinemas": nb_cine,
        "Nombre de monuments": nb_monuments,
        "Valeur foncière moyenne": city['Valeur fonciere']
    })
with open('out.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

