# Created by Alex Crisara on March 26, 2016
# API wrapper for gateCoin trading API
# credentials stored in config.py (which you shouldn't be able to find)

# contains methods to get ETHBTC rate and BTCUSD rate
# might eventually have the ability to query balance of ETH address

# import deps
import requests, json

from objectpath import *

# API url
# no auth is needed
gatecoin_url = "https://www.gatecoin.com/api/Public/LiveTickers"


# objectpath queries
# query for ETHBTC
ETHBTC_query = "$..tickers.*[@.currencyPair is 'ETHBTC'].last[0]"

# query for BTCUSD
BTCUSD_query = "$..tickers.*[@.currencyPair is 'BTCUSD'].last[0]"

def getRate(query, url):
	# fetch api data and parse raw -> json
	apiResp = requests.get(url)
	parsedResp = json.loads(apiResp.text)

	# build tree for objectpath to traverse
	respTree = Tree(parsedResp)

	# apply given objectpath query
	outVal = respTree.execute(query)

	# return query result
	return outVal


# convert value of 1 ETH to USD
def getETHUSD():
	ETHBTC = getRate(ETHBTC_query, gatecoin_url)
	BTCUSD = getRate(BTCUSD_query, gatecoin_url)
	# convert
	valUSD = float(ETHBTC * BTCUSD)

	return valUSD


'''
print('Testing functions')

testETHBTC = getRate(ETHBTC_query, gatecoin_url)
print('\nETH to BTC rate -> %.6f') %testETHBTC

testBTCUSD = getRate(BTCUSD_query, gatecoin_url)
print('\nBTC to USD rate -> %.6f') %testBTCUSD
'''
