import json
from schools.main import parse_data


# create an output json file with the following structure:
# {
#     [
#         {
#             "code Insee": 22385,
#             "Commune": "Plouha",
#             "Nombre d'établissements scolaures": 3
#         },
#         ...
#     ]
# }
data = parse_data()
data = data['code_commune'].value_counts().reset_index()
data.columns = ['code Insee', 'Nombre d\'établissements scolaires']
data = data.rename(columns={'index': 'Commune'})
data = data.to_json(orient='records')
with open('./out.json', 'w') as f:
    f.write(data)
