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

r = m.get(url)
j = json.loads(r.text)
pprint.pprint(r)
pprint.pprint(j)
