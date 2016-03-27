# testing classes in python

# import deps

import time, json, requests

class Ticker(object):
	# in python the __init__ class acts as the constructor
	# need to use abstracted constructor -> one for ONLY latest
	# -> one for latest_price and previous_price
	# will different update methods be needed?
	def __init__(self, name, latest_price, previous_price, time):
		self.name = name
		self.latest_price = latest_price
		# default value set to 1.88
		self.previous_price = 1.88
		self.time = time

	def get_latest_price(self):
		return float(self.latest_price)

	def updateTicker(self, latest_price_update):
		self.name = self.name
		self.previous_price = self.latest_price
		self.latest_price = latest_price_update
		self.time = int(time.time())
 
	# just print out current data in ticker
	def getTicker(self):
		return 'name -> ', self.name, '\nlatest -> ', '%.3f' % self.latest_price, '\nprevious -> ', '%.3f' % self.previous_price, '\ntime -> ', self.time

ticker1 = Ticker("alpha", 11.69, 11.21, int(time.time()))

print('testing methods')

print('\nGetting Latest Price for Ticker1')

print(ticker1.get_latest_price())

print('\nGetting latest data for Ticker1')

print(ticker1.getTicker())

time.sleep(3)

print('\nUpdating ticker1 w/ new info')

# don't need to pass self back into method call on instance of class
ticker1.updateTicker(14.22)

print(ticker1.getTicker())

time.sleep(3)

print('\nUpdating ticker1 again w/ new info')

ticker1.updateTicker(13.25)

print(ticker1.getTicker())

