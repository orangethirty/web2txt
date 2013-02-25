"""Need to get complete list of carriers. And test this.
Note: code is quite unfinished.
right now it runs but /text method is not tested yet.
everything else is.

TODO: finish error messages. test new code.  do 200OK responses.
Clean it up. Update readme. Write docs. :)
Add error reporting to syslog.

Write code to test the /text method. Need to write a 
request in json and POST it with Requests.



"""
import smtplib
import json
from flask import Flask, request, jsonify, Response
from utils import load_config, load_carriers_list, get_carrier 


#api setup
#tested. cofig and carriers working as intended.
CONFIG = load_config()
CARRIERS = load_carriers_list()





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
            data = request.json                  #convert the json into a dict
            carrier = get_carrier(data['carrier'])  #check to see if we support carrier.
            if carrier is not None:
                number = data['number']            
                msg = data['msg']
                TO =  "{0}{1}".format(number, carrier)
                mail = smtplib.SMTP(CONFIG['smtp_address'])
                mail.starttls()
                mail.login(CONFIG['username'], CONFIG['passoword'])
                mail.sendmail(FROM, TO, msg)
                mail.quit()
                return #json response 200 OK
            #if the carrier is not supported or found in the carriers list.
            else: 
                return "http error message with carrier not supported message."
        #if the content type is not json
        else:
            return "http error messahe only JSON accepted." 
    #if the request is not a POST
    else:
        return "the http error message that corresponds to this."


if __name__ == "__main__":
    app.run()
    
    
    
    
    
"""
How the API will work:

This uses the option carriers give to send text messages through email.
You set it up on your server and have it listen at a given port.
Then you make a POST request to /text with the text data as JSON (JSON data structure is to be designed.)
the system takes care of the rest. If the message is sent succesfully you receieve a code 200 from the API.
"""
