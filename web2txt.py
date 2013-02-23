"""Need to get complete list of carriers. And test this.
Note: code is quite unfinished.

TODO: finish error messages. test new code. do json data structure. do 200OK responses.
Clean it up. Update readme. Write docs. :)

have config be loaded from JSON file. easier to change settings.
Add error reporting to syslog.

"""

from flask import Flask, request, jsonify, Response

import smtplib

#List of carriers
CARRIERS = {'tmobile' : '@tmomail.net'}


#email account setup
USERNAME = 'your_username'
PASSWORD = 'our_password'
FROM = 'email@address'

SMTP_ADDRESS = 'smtp.gmail:587'  # as an example for testing.


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
    try:
        if request.method == 'POST':                                 
            if request.headers['Content-Type'] == 'application/json':
                data = request.json                  #convert the json into a dict
                carrier = get_carrier(data['carrier'])  #check to see if we support carrier.
                if carrier is not 'Carrier not supported': #if carrier is not supported we raise the exception below
                    try:                        
                        number = data['number']            
                        msg = data['msg']
                        TO =  "{0}{1}".format(number, carrier)  #need to know how to check for the carrier. Make pe
                        mail = smtplib.SMTP(SMTP_ADDRESS)
                        mail.starttls()
                        mail.login(USERNAME, PASSWORD)
                        mail.sendmail(FROM, TO, msg)
                        mail.quit()
                        return #json response 200 OK
                    except:
                        return 'message could not be sent plus http error code.'
    except:
        return 'some error message'


def get_carrier(carrier):
    try:
        if carrier == 'tmobile':
            return CARRIERS['tmobile']
    except:
        raise ValueError:
            return 'Carrier not supported.'
            
            





if __name__ == "__main__":
    app.run()
    
    
    
    
    
"""
How the API will work:

This uses the option carriers give to send text messages through email.
You set it up on your server and have it listen at a given port.
Then you make a POST request to /text with the text data as JSON (JSON data structure is to be designed.)
the system takes care of the rest. If the message is sent succesfully you receieve a code 200 from the API.
"""
