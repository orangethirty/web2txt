*Docs are in the Wiki.*

web2txt
=========

Send txt messages from a website using an email account.

The project is being developed to help people message others without having to incur in paying for txt as an API 
service. This allows you to run your own texting API with no extra cost.

##How the API works

This uses the option carriers give to send text messages through email.
You set it up on your server and have it listen at a given port.
Then you make a POST request to /text with the text data as JSON (example in docs (Wiki)).
The API takes care of the rest. If the message is sent succesfully you receieve a code 200 from the API.


##Requirements

Flask
smtplib



##License

GNU GPL

Copyright orangethirty@gmail.com


***
List of sms gateways from <a href="https://en.wikipedia.org/wiki/List_of_SMS_gateways">Wikipidea</a>.
