from twilio.rest import TwilioRestClient

account_sid = "AC603bdae185464326b59f75982befc9c5" # Your Account SID from www.twilio.com/console
auth_token  = "65a6f6eb6b11237fbdb9c073b8ea4b99"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+18582636040",    # Replace with your phone number
    from_="+12565308617") # Replace with your Twilio number

# print(message.sid)