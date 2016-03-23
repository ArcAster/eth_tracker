# created by Alex Crisara on March 21, 2016 during database class
# created to test API of gatecoin.com and parse output JSON

# import deps
import requests, json

# define static vars
listings_url = "https://www.gatecoin.com/api/Public/LiveTickers" # auth is not needed

# fetch JSON with GET
api_resp = requests.get(listings_url)

# parse JSON into readable form
parsed_resp = json.loads(api_resp.text)

# prints properly formatted and parsed JSON
#print json.dumps(parsed_resp, sort_keys=True, indent=4, separators=(',', ': '))

# extract ETH to BTC value
# returns current value of 1 ETH in terms of BTC
ETH_to_BTC = [item["last"] for item in parsed_resp
            if item[0]["currencyPair"] ==  "ETHBTC"]
# extract BTC to USD value
# returns value of 1 BTC in terms of USD
