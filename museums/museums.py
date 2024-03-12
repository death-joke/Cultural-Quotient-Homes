#commune, Code Postal, Latitude;Longitude,Nom officiel du musée;
import pandas as pd
from unidecode import unidecode


def parse_data_museums():
    '''Parse data from csv file and return a dataframe with the following columns:
    - Nom officiel du musée : the official name of the museum
    - Commune : the name of the city where the museum is located
    - Code Postal : the postal code of the museum
    - Latitude : the latitude of the museum
    - Longitude : the longitude of the museum'''
    data = pd.read_csv('./museums/liste-et-localisation-des-musees-de-france.csv', sep=';')
    data = data[['Nom officiel du musée', 'Commune', 'Code Postal', 'Latitude', 'Longitude']]
    data = data.drop_duplicates()
    data = data.dropna()
    data['Commune'] = data['Commune'].apply(lambda x: unidecode(x).upper())
    return data


if __name__ == "__main__":
    parse_data_museums().to_csv("museums.csv", sep=';')
