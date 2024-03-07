import pandas as pd

# data from 

def parse_data_schools():
    '''Parse data from csv file and return a dataframe with the following columns:
    - appellation_officielle : the official type of the school
    - denomination_principale : the main denomination of the school
    - libelle_commune : the name of the city where the school is located
    - code_postal_uai : the postal code of the school
    - code_commune : the INSEE code of the city where the school is located'''

    data = pd.read_csv('./schools/data.csv', sep=';', encoding='utf-8')
    data = data[['appellation_officielle', 'denomination_principale', 'libelle_commune', 'code_postal_uai', 'code_commune']]
    return data


if __name__ == "__main__":
    # put it into csv
    parse_data_schools().to_csv('./schools/data_cleaned.csv', index=False, sep=';', encoding='utf-8')