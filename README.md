# Hello_Magento

## Intro:
This is my "Hello World" for hacking around with the Magento2 REST API's.  Apparently, these are Oauth1.  Magento2 also offers an xmlrpc API endpoint, too.


##Reference:
* [Requests-oauthlib](https://github.com/requests/requests-oauthlib) basically does oauth 1 and 2 on top of [Requests](http://docs.python-requests.org/en/master/).  Cool!   
* Magento 2 API Status Codes (and a few samples) [here](https://devdocs.magento.com/guides/v2.2/get-started/gs-web-api-response.html)
* Magento Commerce All API Endpoints: [swagger](https://devdocs.magento.com/swagger/)
* It it mandatory to pass "?searchCriteria[page_size]=" into the API calls where you get a list.  Per this [link](https://community.magento.com/t5/Magento-2-x-Programming/REST-API-Get-all-Products/td-p/21352) anyway.  Otherwise, it fails with a parameter not found eror.
  * If we have to pass a page_size, we'll need to remember to implement a loop to go through the pages.
* Another article about [Magento 2 API](https://amasty.com/blog/how-to-start-with-magento-2-api/) talking about different types of authentication and token generation.
* Encode the JSON string from json.dumps() into utf-8 with this:  line.encode('utf-8')
* ~~Oauth2 [example](https://www.bluehut.net/blog/2012/calling-magento-api-from-python.html) of hitting REST endpoint, but abandoned because Magento is Oauth1~~
* ~~Another [example](https://developer.byu.edu/docs/consume-api/use-api/oauth-20/oauth-20-python-sample-code) of Oauth2 token generation.~~
* [GitHubGist](https://gist.github.com/lloydzhou/98f6fcb69550558e9bdf) - A Magento REST API example with rauth.


##TODO:
* Enable Magento2 API endpoints: [tutoria](lhttps://inviqa.com/blog/magento-2-tutorial-overview-web-api)
* (Not used) Authenticate with Python [Rauth](https://github.com/litl/rauth)
* ~~Observe and Report:  Get list of all customers, all attributes, specific attribute~~
* Start Breaking Stuff:  Use a POST or a PUT or a DELETE to manipulate data in Magento Database.
* Add a specific attribute to a specific SKU or product given a product or sku ID.
* What is special about https://jeff.mh./swagger?apiKey=products#/catalogProductRenderListV1
* Why is a "callback url" in the API integrations setup, and what purpose does that serve?

