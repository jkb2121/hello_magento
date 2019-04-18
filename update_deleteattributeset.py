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
    print("Usage:  update_deleteattributeset.py <config>.yaml")
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


def delete_attribute_set(attribute_set_id):

    url = '{}/V1/products/attribute-sets/{}'.format(api_url, attribute_set_id)
    r = m.get(url)

    j = json.loads(r.text)
    pprint.pprint(j)

    pr = m.delete(url, headers={'Content-type': 'application/json' })

    if pr.status_code == 200:
        print("Aset: {} - Success".format(attribute_set_id))
    else:
        print("Aset: {} - Failed with Code {}".format(attribute_set_id, pr.status_code))


asets = [
    14,
    16,
    18
]

for aset in asets:
    delete_attribute_set(aset)
