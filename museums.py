#commune, Code Postal, Latitude;Longitude,Nom officiel du musée;
import pandas as pd

df = pd.read_csv('liste-et-localisation-des-musees-de-france.csv', sep=';')
df = df[['Nom officiel du musée', 'Commune', 'Code Postal', 'Latitude', 'Longitude']]
df = df.drop_duplicates()
df = df.dropna()
print("juanny")
df.to_csv("museums.csv", sep=';')
