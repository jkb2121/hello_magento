from requests_oauthlib import OAuth1Session, OAuth1
import requests
import pprint
import json
import sys
import yaml
from urllib.parse import quote
from urllib.request import urlretrieve
import html
import csv
#
# Read the Magento API Oauth1 Info from the YAML file.
#
oc_key = oc_secret = oa_token = oa_secret = api_url = ''
inputfile = ''
if len(sys.argv) != 3:
    print("Usage:  create_customer.py <config>.yaml <pricefile>")
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
    inputfile = sys.argv[2]
#
# Create the Oauth1 Session
#
m = OAuth1Session(client_key=oc_key,
                  client_secret=oc_secret,
                  resource_owner_key=oa_token,
                  resource_owner_secret=oa_secret)
# ---------------------------------------------------------------------------------------------------------------------
#
# Add the customer to Magento using the Magento API, given the provided customer record data.
#
def add_customer(email, fname, lname, phone, addr1, addr2, city, state, zip, country):

    # "escape" the forward slash.  Ugh.
    email = email.replace('/', "%2F")
    fname = fname.replace('/', "%2F")
    lname = lname.replace('/', "%2F")
    phone = phone.replace('/', "%2F")
    addr1 = addr1.replace('/', "%2F")
    addr2 = addr2.replace('/', "%2F")
    city = city.replace('/', "%2F")
    state = state.replace('/', "%2F")
    zip = zip.replace('/', "%2F")
    country = country.replace('/', "%2F")

    url = '{}/V1/customers'.format(api_url)
    r = m.get(url)

    if len(addr2) > 0:
        address = "{}, {}".format(addr1, addr2)
    else:
        address = addr1

    j = {
          "customer": {
            "group_id": 1,
            "email": email,
            "firstname": fname,
            "lastname": lname,
            "store_id": 1,
            "website_id": 0,
            "addresses": [
              {
                "region": {
                  "region": state,
                },
                "country_id": country,
                "street": [
                  address
                ],
                "telephone": phone,
                "postcode": zip,
                "city": city,
                "firstname": fname,
                "lastname": lname,
                "default_shipping": True,
                "default_billing": True,
              }
            ],
            "disable_auto_group_change": 0,
            "extension_attributes": {
              "is_subscribed": True
            },
          }
          #   ,
          # "password": "!@!string1231SSSGAAasdfa343"
        }

    pr = m.post(url, json.dumps(j), headers={'Content-type': 'application/json' })

    if pr.status_code == 200:
        print("Sku: {} - Success".format(email))
    else:
        print("Sku: {} - Failed with Code {}".format(email, pr.status_code))
        print("Response:")
        print(pr.text)

# ----------------------------------------------------------------------------------------------------------------------
#
# Hard Coded Test Data
#

# fname = "Integration"
# lname = "Tech"
# email = "integrationtech@github.com"
# phone = "503-555-1212"
# addr1 = "25749 SW Candy Cane Lane"
# addr2 = "Suite 705"
# city = "Wilsonland"
# state = "OX"
# zip = "97071"
# country = "US"

# add_customer(email, fname, lname, phone, addr1, addr2, city, state, zip, country)

# ----------------------------------------------------------------------------------------------------------------------
# Read from the CSV file, and then Add the Customer Record to Magento
#

# with open(inputfile) as csvfile:
#
#     reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
#     i = 0
#     for row in reader:
#         i += 1
#         if row['customers_firstname'] == "":
#             continue
#
#         # Placeholder if you left off anywhere in the file
#         # if i < 3117:
#         #    continue
#
#         # print("Name: {} {}, Email: {}".format(row['customers_firstname'], row['customers_lastname'],
#         #                                       row['customers_email_address']))
#
#         add_customer(row['customers_email_address'], row['customers_firstname'], row['customers_lastname'],
#                      row['customers_telephone'], row['entry_street_address'], row['entry_suburb'],
#                      row['entry_city'], row['zone_name'], row['entry_postcode'], row['countries_iso_code_2'])


customers = ['integrationtech@metacommerce.com']

for customer in customers:
    # print("customer:  {}".format(customer))

    # /V1/customers/search
    url = 'https://www.haikudesigns.com/rest/all/V1/customers/search'

    params = 'searchCriteria[filterGroups][0][filters][0][field]=email&' \
             'searchCriteria[filterGroups][0][filters][0][value]=integrationtech@metacommerce.com&' \
             'searchCriteria[filterGroups][0][filters][0][conditionType]=eq'.format(api_url)

    url = "{}?{}".format(url, quote(params))

    # token_url = 'https://www.haikudesigns.com/rest/V1/integration/admin/token'
    # r = m.post(url)
    #
    # m.token
    #
    # print("status code: {}".format(r.status_code))

    # print("Token: {}".format(m.fetch_access_token(token_url)))

    # headers = {'Authorization': 'Bearer {}'.format(m.token)}
    # sx = requests.get(url, auth=queryoauth, headers=headers)

    url = 'https://www.haikudesigns.com/rest/all/V1/customers/5'

    print("URL: {}".format(url))
    sx = m.get(url)

    print("Status Code: {}".format(sx.status_code))
    pprint.pprint(json.loads(sx.text))