from requests_oauthlib import OAuth1Session
import pprint
import json
import sys
import yaml
from urllib.parse import quote
from urllib.request import urlretrieve
import html
#
# Read the Magento API Oauth1 Info from the YAML file.
#
oc_key = oc_secret = oa_token = oa_secret = api_url = ''
if len(sys.argv) != 3:
    print("Usage:  update_prices.py <config>.yaml <pricefile>")
    exit(1)
else:
    try:
        print("Using Configuration File: " + sys.argv[1])
        with open(sys.argv[1], 'r') as f:
            yml = yaml.load(f)
            oc_key = yml['magento_api_settings']['consumer_key']
            oc_secret = yml['magento_api_settings']['consumer_secret']
            oa_token = yml['magento_api_settings']['access_token']
            oa_secret = yml['magento_api_settings']['access_secret']
            api_url = yml['magento_api_settings']['api_endpoint']

    except IOError:
        print("Error Opening Config File: " + sys.argv[1])
        exit(1)

#
# Create the Oauth1 Session
#
m = OAuth1Session(oc_key,
                  client_secret=oc_secret,
                  resource_owner_key=oa_token,
                  resource_owner_secret=oa_secret)
# ---------------------------------------------------------------------------------------------------------------------

def update_price(sku, price):

    # "escape" the forward slash.  Ugh.
    sku = sku.replace('/', "%2F")

    url = '{}/V1/products/{}'.format(api_url, quote(sku))
    r = m.get(url)

    j = json.loads(r.text)

    if abs(j['price'] - float(price)) < 0.001:
        print("No Update Needed for {} at price {}".format(sku, price))
    else:
        print("About to Update {} from {} to {}".format(sku, j['price'], price))

        j['price'] = price

        data = {"product": j}
        pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })

        if pr.status_code == 200:
            print("Sku: {} - Success".format(sku))
        else:
            print("Sku: {} - Failed with Code {}".format(sku, pr.status_code))



with open(sys.argv[2], "r") as f:
    li = 0
    lines = f.readlines()
    for line in lines:

        if li == 0:
            # Skip Header Row
            li += 1
            continue
        else:
            li += 1

        line = line.strip()

        p = line.split('\t')
        sku = p[0]
        price = p[1]

        update_price(sku, price)
        # print("Set {} to {}".format(sku, price))






