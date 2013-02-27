import json


def load_config():
    """returns configuration as dictionary"""
    with open('config.json', 'r') as f:
        config = json.load(f)
        f.close()
        return config 


def load_carriers():
    """loads the carriers from carriers.json"""
    with open('carriers.json', 'r') as f:
        carriers = json.load(f)
        f.close()
        return carriers


