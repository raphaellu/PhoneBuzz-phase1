from flask import *
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = "AC603bdae185464326b59f75982befc9c5" # Your Account SID from www.twilio.com/console
auth_token  = "65a6f6eb6b11237fbdb9c073b8ea4b99"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

@app.route('/')
def index():
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")
    return str(resp)
    # return render_template('index.html')

@app.route('/success')
def phoneBuzz():
    error = None
    if request.method == 'GET':
        nm = request.args.get('number')
        res = generatePhoneBuzz(int(nm));
        message = client.messages.create(body=', '.join(res),
            to="+18582636040",    # Replace with your phone number
            from_="+12565308617") # Replace with your Twilio number
        return render_template('index.html', result = res)
    return render_template('index.html')

# @app.route('/success', methods=['GET'])
# def success():
#   error = None
#   if request.method == 'GET':
#       nm = request.args.get('number')
#       res = generatePhoneBuzz(int(nm));
#       message = client.messages.create(body=', '.join(res),
#           to="+18582636040",    # Replace with your phone number
#           from_="+12565308617") # Replace with your Twilio number
#   return redirect(url_for('/',result=res))


def generatePhoneBuzz(nm):
    res = []
    for i in range(1, nm+1):
        if (i % 5 == 0 and i % 3 == 0): res.append("Fizz Buzz")
        elif (i % 5 == 0): res.append("Buzz")
        elif (i % 3 == 0): res.append("Fizz")
        else : res.append(str(i))    
    return res
