from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

import smtplib

#List of carriers
TMOBILE = '@tmomail.net'


#email account setup
USERNAME = 'your_username'
PASSWORD = 'our_password'
FROM = 'email@address'


#flask setup
app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html')

#send the txt message	
@app.route("/send", methods=['POST'])
def send():
    if request.method == 'POST':
        number = request.form['number']
        msg = request.form['msg']
        TO =  number + TMOBILE
        mail = smtplib.SMTP('smtp.gmail.com:587')
        mail.starttls()
        mail.login(USERNAME, PASSWORD)
        mail.sendmail(FROM, TO, msg)
        mail.quit()
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
