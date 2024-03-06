import pandas as pd

# data from 

def parse_data():
    '''Parse data from csv file and return a dataframe with the following columns:
    - appellation_officielle : the official type of the school
    - denomination_principale : the main denomination of the school
    - libelle_commune : the name of the city where the school is located
    - code_postal_uai : the postal code of the school
    - code_commune : the INSEE code of the city where the school is located'''

    data = pd.read_csv('data.csv', sep=';')
    data = data[['appellation_officielle', 'denomination_principale', 'libelle_commune', 'code_postal_uai', 'code_commune']]
    return data

print(parse_data())