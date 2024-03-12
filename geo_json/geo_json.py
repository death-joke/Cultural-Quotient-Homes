import geojson


# Path to the geoJSON file

file_path2 = './geo-json/communes-version-simplifiee.geojson'

def parse_geojson():
    file_path = './geo_json/communes-avec-outre-mer.geojson'
    with open(file_path) as f:
        geodata = geojson.load(f)
    return geodata
