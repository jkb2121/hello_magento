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
    print("Usage:  update_attributesets.py <config>.yaml")
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


def update_attribute_set(sku, attribute_set_id):

    # "escape" the forward slash.  Ugh.
    sku = sku.replace('/', "%2F")

    url = '{}/V1/products/{}'.format(api_url, quote(sku))
    r = m.get(url)

    j = json.loads(r.text)
    # pprint.pprint(j)
    j['attribute_set_id'] = attribute_set_id

    data = {"product": j}
    pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })

    if pr.status_code == 200:
        print("Sku: {} - Success".format(sku))
    else:
        print("Sku: {} - Failed with Code {}".format(sku, pr.status_code))


# skus = ['1253', 'F-SOHO-4D-N.WAL']
# # , '1254'
# # '1255',
# # '1256',
# # '1187.',
# # '1207',
# # '1209']
#
# for sku in skus:
#     update_attribute_set(sku)

with open("work/attribute_set_update.txt", "r") as f:
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
        attribute_set = p[1]

        update_attribute_set(sku, attribute_set)
        print("Set {} to {}".format(sku, attribute_set))
