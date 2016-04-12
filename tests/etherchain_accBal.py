# created by Alex Crisara
# testing etherchain.org API to gather eth acct. balance

import requests, json

from objectpath import *


# ethereum address used to query value from
user_eth_addr = "0x5c6680bef7556aae95b5fd073ddb35a0ea59c601"

# url for etherchain.org BALANCE API
etherchain_url = "https://etherchain.org/api/account/" + user_eth_addr


# query for current acct balance
ACCT_BAL_query = "$..data[0].balance"

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

test = getRate(ACCT_BAL_query, etherchain_url)

print type(test)

test = float(test) / pow(10, 18)

print test

print type(test)
