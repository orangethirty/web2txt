import json

def load_config():
    """returns configuration as dictionary"""
    with open('config.json', 'r') as f:
        config = json.load(f)
        f.close()
        return config 

def load_carriers_list():
    """loads the carriers from carriers.json"""
    with open('carriers.json', 'r') as f:
        carriers = json.load(f)
        f.close()
        return carriers
        
        
def get_carrier(carrier):
    """gets the carrier data from the carriers dict. 
       If carrier is not found, returns None type.
    """
    if carrier == 'tmobile':
        return CARRIERS['tmobile']
    else:
        return None
