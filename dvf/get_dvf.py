import pandas as pd
import zipfile

with zipfile.ZipFile('dvf/dataset.zip', 'r') as zip_ref:
    zip_ref.extractall('dvf')

#load file into a dataframe
df = pd.read_csv('dvf/dataset/valeursfoncieres-2021.txt', sep='|', encoding='latin1', dtype={18: str, 23: str, 24: str, 26: str, 28: str, 29: str, 31: str, 33: str, 41: str})
df['Valeur fonciere'] = df['Valeur fonciere'].str.replace(',', '.').astype(float)
valeurs_foncieres = df[['Valeur fonciere', 'Code postal', 'Commune', 'Code departement', 'Code commune']]
print(valeurs_foncieres.head())

#group by code postal and commune
moyenne_par_commune = valeurs_foncieres.groupby(['Code departement', 'Code commune'])['Valeur fonciere'].mean().reset_index()
moyenne_par_commune['Code INSEE'] = moyenne_par_commune['Code departement'] + moyenne_par_commune['Code commune'].apply(lambda x: f'{x:03}')
print(moyenne_par_commune.head())

#save the result in a csv file
moyenne_par_commune.to_csv('dvf/dataset/valeurs_foncieres_grouped.csv', index=False)