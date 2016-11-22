from flask import *
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = "AC603bdae185464326b59f75982befc9c5" # Your Account SID from www.twilio.com/console
auth_token  = "65a6f6eb6b11237fbdb9c073b8ea4b99"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phonebuzz')
def phoneBuzz():
    resp = twilio.twiml.Response()
    # ask user to enter a num for game
    with resp.gather(action="/handle_input", method="POST", timeout=10) as g:
        g.say("Please enter a number to start fizz buzz game, followed by the pound sign.")
    return str(resp)

@app.route('/handle_input')    
def handle_input():
    nm = request.values.get('Digits', None)
    resp = twilio.twiml.Response()
    if nm.isdigit():  # if input is valid
        res = generatePhoneBuzz(int(nm))
        res.say(", ".join(res) + "</Say><Say>,,,,Game finished. Goodbye!</Say></Response>")
    else: # if input is invalid, ask for re-entering the num
        res.say("You did not enter a valid number.")
        return redirect("/phonebuzz")

    
def generatePhoneBuzz(nm):
    res = []
    for i in range(1, nm+1):
        if (i % 5 == 0 and i % 3 == 0): res.append("Fizz Buzz")
        elif (i % 5 == 0): res.append("Buzz")
        elif (i % 3 == 0): res.append("Fizz")
        else : res.append(str(i))    
    return res
