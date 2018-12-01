# Hello_Magento

## Intro:
This is my "Hello World" for hacking around with the Magento2 Rest API's.  Apparently, these are Oauth1


##Reference:
* Requests_oauthlib basically does oauth 1 and 2 on top of Requests.  Cool:  https://github.com/requests/requests-oauthlib 
* Magento 2 API Status Codes (and a few samples) https://devdocs.magento.com/guides/v2.2/get-started/gs-web-api-response.html
* Magento Commerce Swagger: https://devdocs.magento.com/swagger/
* It it mandatory to pass "?searchCriteria[page_size]=" into the API calls where you get a list.  Per this [link](https://community.magento.com/t5/Magento-2-x-Programming/REST-API-Get-all-Products/td-p/21352) anyway.  Otherwise, it fails with a parameter not found eror.
  * If we have to pass a page_size, we'll need to remember to implement a loop to go through the pages.


##TODO:
* Enable Magento2 API endpoints: https://inviqa.com/blog/magento-2-tutorial-overview-web-api
* (Not used) Authenticate with Python Rauth: https://github.com/litl/rauth
* Get list of all customers
* Get list of all attributes
* Get a specific attribute

