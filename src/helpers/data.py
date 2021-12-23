import json
from os.path import exists

json_file = 'src/helpers/data.json'

def set_value(key, value):
    data = {}

    if not exists(json_file):
        with open(json_file, 'a') as f:
            f.write("{}")

    with open(json_file, 'r') as f:
        data = json.load(f)
        data[key] = value

    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def get_value(key):
    with open(json_file, 'r') as f:
        try:
            data = json.load(f)
            return data[key]
        except:
            return None
