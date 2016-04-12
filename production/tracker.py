# Created by Alex Crisara on March 26, 2016
# sends SMS updates when the price of Ethereum crypto changes ~%

# import deps
import time

from twilio.rest import TwilioRestClient

from fetcher import *

# import super secret credentials
from config import *


# init twilio api client
twilio_client = TwilioRestClient(twilio_account_cred, twilio_token_cred)

# all ticker related things happen here
# price field is value of 1 ether in USD
class Ticker(object):
	# previous_price is hard-coded in __init__
	def __init__(self, name, latest_price, previous_price, time):
		self.name = name
		self.latest_price = latest_price
		self.previous_price = 1.88
		self.time = time

	def get_latest_price(self):
		return float(self.latest_price)

	def updatePrice(self, latest_price_update):
		self.name = self.name
		self.previous_price = self.previous_price
		self.latest_price = latest_price_update
		self.time = int(time.time())

	def thresholdUpdate(self):
		self.name = self.name
		self.previous_price = self.latest_price
		self.latest_price = self.latest_price
		self.time = int(time.time())

	def getData(self):
		return self

# creating primary instance of ticker
alphaTick = Ticker('alpha', 10.01, 1.88, int(time.time()))

# calculate percent change of input values
def percChange(ltst, prev):
	perc = ((ltst-prev) / ltst) * 100
	return perc

def sendSMS(msg):
	message = twilio_client.messages.create(to=user_num, from_=twilio_origin_cred, body=msg)

# if %change threshold met, decide what message to send
def makeSMS(obj, chng):
	# positive change
	if(chng > 0):
		msg = '>> ETH UP | $' + format(obj.latest_price, '.2f') + ' | @ $' + format((obj.latest_price * getAcctBal()), '.2f') + ' <<'
		return msg

	# negative change
	else:
		msg = '>> ETH DOWN | $' + format(obj.latest_price, '.2f') + ' | @ $' + format((obj.latest_price * getAcctBal()), '.2f') + ' <<'
		return msg



# update loop
while(True):
	
	try:
		alphaTick.updatePrice(getETHUSD())
		obj = alphaTick.getData()
		#print '-----------'
		#print obj.latest_price

		chng = percChange(obj.latest_price, obj.previous_price)
		print('price - %.3f | shift -  %.3f') %(obj.latest_price, chng)

		if(abs(chng) >= 2.0):
			alphaTick.thresholdUpdate()
			msg = makeSMS(obj, chng)
			print msg
			sendSMS(msg)
	except:
		print '\n--WEIRD PARSE ERROR --\n'
		pass
	
	time.sleep(90)


