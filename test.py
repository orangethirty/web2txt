#A little script to help test the API

import json
import requests

url = ''                           #url where your API lives.
carrier = ''                       #note: check list of supported carriers in carriers.json
number = ''                        #number with area code
message = ''                       #note that SMS has a size limit.
payload = {'carrier' : carrier, 'number' : number, 'msg' : message}
headers = {'content-type' : 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print r
