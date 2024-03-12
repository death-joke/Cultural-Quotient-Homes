from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
import csv
import json
import pandas as pd

# response = requests.get("https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets/etablissements-cinematographiques/records?select=nom%2C%20region_administrative%2C%20commune%2C%20code_insee%2C%20entrees_2022%2C%20latitude%2C%20longitude%2C%20geolocalisation&order_by=commune")
# print(response.status_code)
# print(response.json())

def remove_duplicates_and_save(entities, output_filename):
    entities_as_json = [json.dumps(entity) for entity in entities]
    df = pd.DataFrame(entities_as_json, columns=['json'])
    df.drop_duplicates(inplace=True)
    cleaned_entities = [json.loads(entity) for entity in df['json']]
    with open(output_filename, 'w') as outfile:
        outfile.write(json.dumps(cleaned_entities))


# Traitement des cinémas
columns_to_exclude_cinema = ["regioncnc", "ndeg_auto", "adresse", "population_de_la_commune", "dep", "ndeguu", "unite_urbaine",
                             "population_unite_urbaine", "situation_geographique", "ecrans", "fauteuils", "semaines_d_activite",
                             "seances", "entrees_2021", "evolution_entrees", "tranche_d_entrees", "programmateur", "latitude", "longitude",
                             "categorie_art_et_essai", "label_art_et_essai", "genre", "multiplexe", "zone_de_la_commune", "nombre_de_films_programmes",
                             "nombre_de_films_inedits", "nombre_de_films_en_semaine_1", "pdm_en_entrees_des_films_francais",
                             "pdm_en_entrees_des_films_americains", "pdm_en_entrees_des_films_europeens", "pdm_en_entrees_des_autres_films",
                             "films_art_et_essai", "pdm_en_entrees_des_films_art_et_essai", "ae"]

with open('./cultural/etablissements-cinematographiques.json', 'r') as f:
    entities_cine = json.load(f)

for entity in entities_cine:
    for key in columns_to_exclude_cinema:
        entity.pop(key)

remove_duplicates_and_save(entities_cine, "./cultural/cinema_intermediaire.json")

# Traitement des bibliothèques
columns_to_exclude_bibliotheques = ["code_bib", "surface", "amplitude_horaire", "libelle_2", "complement", "adresse", "code_region",
                                     "code_departement", "cedex", "population_commune", "longitude", "latitude", "statut",
                                     "type_adresse", "nombre_de_salaries", "nombre_de_benevoles"]

with open('./cultural/adresses-des-bibliotheques-publiques.json', 'r') as f2:
    entities_bibli = json.load(f2)

for entity in entities_bibli:
    for key in columns_to_exclude_bibliotheques:
        entity.pop(key)

remove_duplicates_and_save(entities_bibli, "./cultural/biblio_intermediaire.json")

# Traitement des monuments
columns_to_exclude_monuments = ["annee", "region", "code_insee_region", "departement", "gratuit", "payant", "total", "code_insee_departement"]

with open('./cultural/frequentation-des-monuments-nationaux.json', 'r') as f3:
    entities_monuments = json.load(f3)

for entity in entities_monuments:
    for key in columns_to_exclude_monuments:
        entity.pop(key)

remove_duplicates_and_save(entities_monuments, "./cultural/monuments_intermediaire.json")


