import pandas as pd


def parse_cultural_data():
    '''Parse data from json files and return a tuple of dataframes with the following order:
    - 1: the dataframe of public libraries
    - 2: the dataframe of cinemas
    - 3: the dataframe of national monuments
    '''
    bibli = pd.read_json('./cultural/biblio_intermediaire.json')
    cine = pd.read_json('./cultural/cinema_intermediaire.json')
    monuments = pd.read_json('./cultural/monuments_intermediaire.json')

    return bibli, cine, monuments