from requests_oauthlib import OAuth1Session
import pprint
import json
import sys
import yaml

#
# Read the Magento API Oauth1 Info from the YAML file.
#
oc_key = oc_secret = oa_token = oa_secret = api_url = ''
if len(sys.argv) != 2:
    print("Usage:  hello_magento.py <config>.yaml")
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

#
# Now run some tests and lookups...
#

# Call some individual customers
# url = '{}/V1/customers/2'.format(api_url)
# url = '{}/V1/customers/1'.format(api_url)
# url = '{}/V1/customers/search?searchCriteria%5Bpage_size%5D=100'.format(api_url)

# Get a specific product by SKU:
# sku = "F-AZAR-DR-SABL"
# url = '{}/V1/products/{}'.format(api_url, sku)

# Request a specific attribute set or list of attribute sets
# url = '{}/V1/products/attribute-sets/9'.format(api_url)
# url = '{}/V1/products/attribute-sets/sets/list?searchCriteria%5Bpage_size%5D=100'.format(api_url)

# Request list of Attributes
# url = '{}/V1/categories/attributes?searchCriteria%5Bpage_size%5D=100'.format(api_url)

# Request list of Products
# url = '{}/V1/products?searchCriteria%5Bpage_size%5D=100'.format(api_url)

# Request specific SKU
# sku = 'WEL-BOLS-FLAT-18-S.GRN'
# url = '{}/V1/products/{}'.format(api_url, sku)
# #url = '{}/V1/products/{}/options'.format(api_url, sku)
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)

# See Color:  {'attribute_code': 'color', 'value': '30'},

# url = '{}/V1/configurable-products/{}/options/all'.format(api_url, "1436")
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)
# # List of Colors associated to Configured Product: 1436


# url = '{}/V1/configurable-products/{}/children'.format(api_url, "1436")
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)
# # All Children and attribute values

# Get Monster List of all Attributes
# url = '{}/V1/products/attributes?searchCriteria%5Bpage_size%5D=100'.format(api_url)
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)


# Request specific Product 1000 (Akita Platform Bed)
# sku = '1000'
# url = '{}/V1/products/{}'.format(api_url, sku)
# #url = '{}/V1/products/{}/options'.format(api_url, sku)
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)
#
# for attrib in j['custom_attributes']:
#     print("Attribute: {} - {}".format(attrib['attribute_code'], attrib['value']))

# j['custom_attributes'].append({'attribute_code': 'platform_bed', 'value': '1'})
# print("--------------------------------------------------")
# pprint.pprint(j)
#
# data = {"product": j}
# pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })
# print("--------------------------------------------------")
# pprint.pprint(pr.text)


# Request specific SKU (Akita Platform Bed - King)
# sku = 'F-AKIT-K'
# url = '{}/V1/products/{}'.format(api_url, sku)
# #url = '{}/V1/products/{}/options'.format(api_url, sku)
# r = m.get(url)
# j = json.loads(r.text)
# pprint.pprint(r)
# pprint.pprint(j)
#
# found = 0
# for attrib in j['custom_attributes']:
#     print("Attribute: {} - {}".format(attrib['attribute_code'], attrib['value']))
#
#     if attrib['attribute_code'] == 'wood_type':
#         attrib['value'] = '184'
#         found = 1
#
# if found == 0:
#     j['custom_attributes'].append({'attribute_code': 'wood_type', 'value': ''})
#
# print("--------------------------------------------------")
# pprint.pprint(j)
#
# data = {"product": j}
# pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })
# print("--------------------------------------------------")
# pprint.pprint(pr.text)
#
# 'options': [{'label': ' ', 'value': ''},
#                         {'label': 'Acacia', 'value': '182'},
#                         {'label': 'Bamboo', 'value': '181'},
#                         {'label': 'Oak', 'value': '183'},
#                         {'label': 'Walnut', 'value': '184'}]

# ----------------------------------------------------------------------------------------------------------------------
# Attempting Price Changes via API
# We'll have a list of SKU to Price
#
# sku = 'F-RAKU-F-D.WAL'
# new_price = 849
#
#
# # Request SKU
# url = '{}/V1/products/{}'.format(api_url, sku)
# r = m.get(url)
# j = json.loads(r.text)
#
# pprint.pprint(j)
#
# print("Price = {}".format(j['price']))
#
# j['price'] = new_price
#
# data = {"product": j}
# pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })
#
# pprint.pprint(pr)

# ----------------------------------------------------------------------------------------------------------------------
# Attempting To Change Virtual to Simple via API
# We'll have a list of SKU to Price

sku = 'F-AZAR-HC-CARA'

# Request SKU
url = '{}/V1/products/{}'.format(api_url, sku)
r = m.get(url)
j = json.loads(r.text)

pprint.pprint(j)

print("Price = {}".format(j['price']))

j['weight'] = 150
j['type_id'] = 'simple'

data = {"product": j}
pr = m.put(url, json.dumps(data), headers={'Content-type': 'application/json' })

pprint.pprint(pr)


