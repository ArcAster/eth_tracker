# created by Alex Crisara on March 21, 2016 during database class
# created to test API of gatecoin.com and parse output JSON

# import deps
import requests, json

from objectpath import *

# define static vars
listings_url = "https://www.gatecoin.com/api/Public/LiveTickers" # auth is not needed

waitVal = 1 # long to wait between terminal update

# fetch JSON with GET
api_resp = requests.get(listings_url)

# parse JSON into readable form
parsed_resp = json.loads(api_resp.text)

# convert info into tree (evenutally this will be a generalized function)
# uses objectpath to build traversable tree
coinTree=Tree(parsed_resp)

# prints properly formatted and parsed JSON
#print json.dumps(parsed_resp, sort_keys=True, indent=4, separators=(',', ': '))

# extract ETH to BTC value
# returns current value of 1 ETH in terms of BTC
ETHBTC_rate = "$..tickers.*[@.currencyPair is 'ETHBTC'].last[0]"

# extract BTC to USD value
# returns value of 1 BTC in terms of USD
BTCUSD_rate = "$..tickers.*[@.currencyPair is 'BTCUSD'].last[0]"

#print("ETHBTC -> %.3f \nBTCUSD -> %.3f") %(ETHBTC_rate, BTCUSD_rate)

# tickerUpdate -- updates ticker with given objectpath query
def tickerUpdate(OP_query)
