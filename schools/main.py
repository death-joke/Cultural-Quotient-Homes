import pandas as pd

# data from 

def parse_data():
    data = pd.read_csv('data.csv', sep=';')
    data = data[['appellation_officielle', 'denomination_principale', 'libelle_commune', 'code_postal_uai']]
    return data

print(parse_data())