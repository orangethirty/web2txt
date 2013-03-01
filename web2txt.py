#web2txt
#License: GNU GPL
#copyright 2013 orangethirty@gmail.com

import smtplib
from flask import Flask, request, jsonify, Response, json
from utils import load_config, load_carriers, logging


#flask setup
app = Flask(__name__)

#port number you will be listening at. change to fit your needs.
PORT = 5000 


@app.route("/")
def index():
    return 'web2txt API'


#send the txt message	
@app.route("/text", methods=['POST'])
def send_text():
    """Sends the txt message from data passed through POST."""
                                
    if request.headers['Content-Type'] == 'application/json':
        #converts json to python dict
        data = request.json
        #get list of carriers from carriers.json                      
        config = load_config()
        carriers = load_carriers() 
        
        #authenticate request
        if data['api_key'] == config['api_key']:
            
            if data['carrier'] in carriers:
                #prepare the message
                carrier_choice = data['carrier']
                carrier = carriers[carrier_choice]
                number = data['number']            
                msg = data['msg']
                to =  "{0}{1}".format(number, carrier)
                sender = config['from']
                #sends the actual message
                mail = smtplib.SMTP(config['smtp_address'])
                mail.starttls()
                mail.login(config['username'], config['password'])
                mail.sendmail(sender, to, msg)
                mail.quit()
                #prepare the json response.
                log = "Message: '{0}' was sent succesfuly sent to '{1}'.".format(msg, to)
                logging(log)
                resp = {"response" : log}
                response = Response(json.dumps(resp), status=200, mimetype='application/json')
                return response
        
        #if the carrier is not supported or found in the carriers list.
        else: 
            log = "Carrier not supported."
            #log to web2txt.log file
            logging(log)
            resp = {"response" : log}
            response = Response(json.dumps(resp), status=404, mimetype='application/json')
            return response
    
    #if the content type is not json
    else:
        log = "Wrong request content-type. API only support JSON"
        #log to web2txt.log file
        logging(log)
        resp = {"response" : log}
        response = Response(json.dumps(resp), status=415, mimetype='application/json')
        return response 


if __name__ == "__main__":
    #if you need to debug, replace the line below with: app.run(port=PORT, debug=True)
    app.run(port=PORT)
