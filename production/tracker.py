# Created by Alex Crisara on March 26, 2016
# sends SMS updates when the price of Ethereum crypto changes ~%

# import deps
import time, twilio

from fetcher import *

# import super secret credentials
from config import *

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
		self.previous_price = self.latest_price
		self.latest_price = latest_price_update
		self.time = int(time.time())

	def getData(self):
		return self

# creating primary instance of ticker
alphaTick = Ticker('alpha', 10.01, 1.88, int(time.time()))

# calculate percent change of input values
def percChange(ltst, prev):
	perc = ((prev - ltst) / ltst) * 100
	return perc

# update loop
while(True):
	alphaTick.updatePrice(getETHUSD())
	latest = alphaTick.getData()
	print latest.latest_price

	chng = percChange(latest.latest_price, latest.previous_price)
	print chng
	time.sleep(5)


