import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ASSETS_DIR = os.path.join(ROOT_DIR, 'sanatio/assets')


def load_json(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f'File {filename} not found')

    if not filename.endswith('.json'):
        raise ValueError('Filename must be a json file')

    with open(os.path.join(filename), 'r', encoding="utf-8") as f:
        return json.load(f)


def load_asset(filename):
    return load_json(os.path.join(ASSETS_DIR, filename))


country_json = load_asset('country.json')
regexs_dict = load_asset('regex.json')
