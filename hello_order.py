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
if len(sys.argv) != 2:
    print("Usage:  hello_order.py <config>.yaml")
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

# This is a "good" working get_orders() without getting crazy with searchCriteria
def good_get_orders():
    url = "{}/V1/orders?searchCriteria=entity_id&limit=50".format(api_url)

    r = m.get(url)
    j = json.loads(r.text)

    return j["items"]


# Example of SearchCriteria using an OR within the filter_group
# the urllib.parse.quote function doesn't filter things properly for Magento 2
# Just change the [ and ] characters to their html equivalents and it works
# YMMV with any other bad data.  I think the = and & getting encoded jacked it up.
def get_orders():

    sc = "searchCriteria[filter_groups][0][filters][0][field]=status&" \
         "searchCriteria[filter_groups][0][filters][0][value]=pending&" \
         "searchCriteria[filter_groups][0][filters][0][conditionType]=eq&" \
         "searchCriteria[filter_groups][0][filters][1][field]=status&" \
         "searchCriteria[filter_groups][0][filters][1][value]=canceled&" \
         "searchCriteria[filter_groups][0][filters][1][conditionType]=eq"

    print("Unquoted: {}".format(sc))
    print("Quoted: {}".format(quote(sc)))

    sc = sc.replace('[', '%5B')
    sc = sc.replace(']', '%5D')

    print("New SC: {}".format(sc))

    url = "{}/V1/orders?{}&limit=50".format(api_url, sc)
    r = m.get(url)

    j = json.loads(r.text)

    # pprint.pprint(j)
    return j["items"]

# print("Getting Order: {}".format(order_id))
orders = get_orders()

i = 0
for order in orders:
    i += 1
    print("-------------------------------------")
    print("{}. Order:".format(i))
    print("Entity: {}".format(order["entity_id"]))
    print("Increment: {}".format(order["increment_id"]))
    print("State / Status:  {} / {}".format(order["state"], order["status"]))
    print("Base Total: {}".format(order["base_total_due"]))
    print("Total Due: {}".format(order["total_due"]))

    try:
        print("Total Paid: {}".format(order["total_paid"]))
    except:
        print("Total Paid: Not Paid")
    # pprint.pprint(order["payment"])

    # pprint.pprint(order)


