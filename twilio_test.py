# test file for Twilio API

# import credentials from config.py
from config import *

# import dependencies from twilio
from twilio.rest import TwilioRestClient

# init credentials for twilio API
account = twilio_account_cred
token = twilio_token_cred
origin_number = twilio_origin_cred
dest_number = user_num

# init twilio API client
client = TwilioRestClient(account, token)

# prepare message
# whenever below is called an SMS message is sent
message = client.messages.create(to=dest_number, from_=twilio_origin_cred,
                                 body="TEST TRANSMISSION!")
