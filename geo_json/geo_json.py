import geojson
import os



# Path to the geoJSON file

file_path2 = './geo-json/communes-version-simplifiee.geojson'

def parse_geojson():
    file_path = './geo_json/communes-avec-outre-mer.geojson'
    with open(file_path) as f:
        geodata = geojson.load(f)
    return geodata

def parse_light_geojson():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path2 = os.path.join(dir_path, 'light_geodata.geojson')
    with open(file_path2) as f:
        geodata = geojson.load(f)
    return geodata


