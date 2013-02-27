import json
from time import strftime


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


def logging(log):
    """simple logging function. logging string as parameter."""
    with open('web2txt.log', 'a') as f:
        debug_log = "web2txt debug message: {0} * {1} \n".format(strftime("%Y-%m-%d %H:%M:%S"), log)
        f.write(debug_log)
        f.close
