import pandas as pd

# data from 

def parse_data():
    data = pd.read_csv('data.csv', sep=';')
    return data

print(parse_data())