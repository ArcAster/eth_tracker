# Created by Alex Crisara on March 26, 2016
# API wrapper for gateCoin trading API
# credentials stored in config.py (which you shouldn't be able to find)

# contains methods to get ETHBTC rate and BTCUSD rate
# might eventually have the ability to query balance of ETH address

# import deps

# import fancy pyOpenSSL and inject to urllib3
import urllib3
import urllib3.contrib.pyopenssl 
urllib3.contrib.pyopenssl.inject_into_urllib3() 

import requests, json

from objectpath import *

# import super secret credentials
from config import *



# TEST VAL
user_eth_addr = "0x5c6680bEF7556AAe95B5fD073DDb35a0EA59C601"

# API url
# no auth is needed
gatecoin_url = "https://www.gatecoin.com/api/Public/LiveTickers"
etherchain_url = "https://etherchain.org/api/account/" + user_eth_addr

# objectpath queries
# query for ETHBTC
ETHBTC_query = "$..tickers.*[@.currencyPair is 'ETHBTC'].last[0]"

# query for BTCUSD
BTCUSD_query = "$..tickers.*[@.currencyPair is 'BTCUSD'].last[0]"

# query for current acct balance
BAL_query = "$..data[0].balance"

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

def getAcctBal():
	cur_bal = getRate(BAL_query, etherchain_url)

	# convert from Wei to Ether (10^18 Wei in 1 Ether)
	balance = float(cur_bal) / pow(10, 18)

	return balance


print('Testing functions')

testETHBTC = getRate(ETHBTC_query, gatecoin_url)
print('\nETH to BTC rate -> %.6f') %testETHBTC

testBTCUSD = getRate(BTCUSD_query, gatecoin_url)
print('\nBTC to USD rate -> %.6f') %testBTCUSD

print('\n Testing eth balance')

print('type for ethUSD')
print(getETHUSD())

print('\n output for getAcctBal')
print(getAcctBal())
