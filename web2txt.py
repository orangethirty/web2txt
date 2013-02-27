"""
Note: code is tested and working, but unfinished.

TODO: 
Clean it up. Update readme. Write docs. :)
Add error reporting to syslog.
"""


import smtplib
from flask import Flask, request, jsonify, Response, json
from utils import load_config, load_carriers 


#flask setup
app = Flask(__name__)
PORT = 5000 #port number you will be listening at. change to fit your needs


@app.route("/")
def index():
    return 'web2txt API'

#send the txt message	
@app.route("/text", methods=['POST'])
def send_text():
    """Sends the txt message from data passed through POST."""
    
    if request.method == 'POST':                                 
        
        if request.headers['Content-Type'] == 'application/json':
            #converts json to python dict
            data = request.json
            #get list of carriers from carriers.json                      
            carriers = load_carriers() 
            
            if data['carrier'] in carriers:
                #prepare the message
                number = data['number']            
                msg = data['msg']
                to =  "{0}{1}".format(number, carrier)
                CONFIG = load_config()
                FROM = CONFIG['from']
                #sends the actual message
                mail = smtplib.SMTP(CONFIG['smtp_address'])
                mail.starttls()
                mail.login(CONFIG['username'], CONFIG['password'])
                mail.sendmail(FROM, to, msg)
                mail.quit()
                #prepare the json response to your app.
                log = "Message: '{0}' was sent succesfuly sent to '{1}'.".format(msg, to)
                resp = {"response" : log}
                response = Response(json.dumps(resp), status=200, mimetype='application/json')
                return response
            
            #if the carrier is not supported or found in the carriers list.
            else: 
                log = "Carrier not supported."
                resp = {"response" : log}
                response = Response(json.dumps(resp), status=404, mimetype='application/json')
                return response
        
        #if the content type is not json
        else:
            log = "Wrong request content-type. API only support JSON."
            resp = {"response" : log}
            response = Response(json.dumps(resp), status=415, mimetype='application/json')
            return response 
    
    #if the request is not a POST. note that flask handles this but included anyways. 
    else:
        log = "Method Not Allowed. The method GET is not allowed for the requested URL."
        resp = {"response" : log}
        response = Response(json.dumps(resp), status=405, mimetype='application/json')
        return response


if __name__ == "__main__":
    #if you need to debug, replace the line below with: app.run(debug=True)
    app.run()
    
