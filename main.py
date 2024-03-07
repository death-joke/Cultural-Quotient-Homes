import json
from tqdm.auto import tqdm
from schools.main import parse_data_schools
from museums.museums import parse_data_museums
from dvf.get_dvf import parse_data_dvf


# create an output json file with the following structure:
# {
#     [
#         {
#             "code Insee": 22385,
#             "Commune": "Plouha",
#             "Nombre d'établissements scolaures": 3,
#             "Nombre de musées": 1,
#             "Valeur foncière moyenne": 200000
#         },
#         ...
#     ]
# }
data = []
schools = parse_data_schools()
print("schools parsed")
museums = parse_data_museums()
print("museums parsed")
dvf = parse_data_dvf()
print("dvf parsed")
for _, city in tqdm(dvf.iterrows(), total=len(dvf)):
    nb_schools = schools[schools['code_commune'] == city['Code commune']].shape[0]
    nb_museums = museums[(museums['Commune'] == city['Commune']) & (museums['Code Postal'] == city['Code postal'])].shape[0]

    data.append({
        "code Insee": city['Code commune'],
        "Commune": city['Commune'],
        "Code postal": city['Code postal'],
        "Nombre d'établissements scolaires": nb_schools,
        "Nombre de musées": nb_museums,
        "Valeur foncière moyenne": city['Valeur fonciere']
    })
with open('out.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

