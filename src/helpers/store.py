import json
from os.path import exists

json_file = "src/helpers/store.json"


def __read_file(json_file):
    if not exists(json_file):
        with open(json_file, "a") as f:
            f.write("{}")

    with open(json_file, "r") as f:
        return f.read()


def __write_to_file(json_file, data):
    with open(json_file, "w") as f:
        f.write(data)


def set_value(key, value):
    file_text = __read_file(json_file)
    data = json.loads(file_text)
    data[key] = value

    __write_to_file(json_file, json.dumps(data))


def get_value(key):
    try:
        file_text = __read_file(json_file)
        data = json.loads(file_text)
        return data[key]
    except:
        return None
