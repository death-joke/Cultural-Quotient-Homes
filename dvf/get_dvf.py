import pandas as pd
import zipfile


def parse_data_dvf():
    '''Parse data from csv file and return a dataframe with the following columns:
    - Valeur fonciere : the value of the property
    - Code postal : the postal code of the property
    - Commune : the name of the city where the property is located
    - Code departement : the department code of the property
    - Code commune : the city code of the property'''
    with zipfile.ZipFile('./dvf/dataset.zip', 'r') as zip_ref:
        zip_ref.extractall('./dvf')
    df = pd.read_csv('./dvf/dataset/valeursfoncieres-2021.txt', sep='|', encoding='latin1', dtype={18: str, 23: str, 24: str, 26: str, 28: str, 29: str, 31: str, 33: str, 41: str})
    df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)
    valeurs_foncieres = df[['Valeur fonciere', 'Code postal', 'Commune', 'Code departement', 'Code commune']]
    moyenne_par_commune = valeurs_foncieres.groupby(['Code departement', 'Code commune', 'Code postal', 'Commune'])['Valeur fonciere'].mean().reset_index()
    moyenne_par_commune['Code INSEE'] = moyenne_par_commune['Code departement'] + moyenne_par_commune['Code commune'].apply(lambda x: f'{x:03}')
    return moyenne_par_commune


if __name__ == "__main__":
    #save the result in a csv file
    parse_data_dvf().to_csv('./dvf/dataset/valeurs_foncieres_grouped.csv', index=False)