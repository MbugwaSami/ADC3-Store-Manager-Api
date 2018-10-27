[![Build Status](https://travis-ci.org/MbugwaSami/ADC3-Store-Manager-Api.svg?branch=develop)](https://travis-ci.org/MbugwaSami/ADC3-Store-Manager-Api)
[![Coverage Status](https://coveralls.io/repos/github/MbugwaSami/ADC3-Store-Manager-Api/badge.svg)](https://coveralls.io/github/MbugwaSami/ADC3-Store-Manager-Api)
[![Maintainability](https://api.codeclimate.com/v1/badges/983deaa061360fd47d75/maintainability)](https://codeclimate.com/github/MbugwaSami/ADC3-Store-Manager-Api/maintainability)
# ADC3-Store-Manager-Api


This repository  contains API endpoints for  Store Manager application. Store Manager application is an application that helps small scale stalls manage their sales and inventory. The application store data in a postgres database.The application has two level of users, the store owner who is also the admin and the store attendant.
The Admin is responsible for adding new products and creating user accounts and the store attendant is responsible for making new sales.

### The minimum required endpoint are  
| Endpoint | Description |
| --- | --- |
|GET /Fetch all products	| This endpoint gets all available products in the system.Accesed to both the Admin and the store attendant|
|GET /Fetch a single product record	| This endpoint gets a specific product using the product’s id. Accesed by the Admin and store attendant|
|GET /Fetch all sale records.|This endpoint gets all sales done by all the store attendants.Accesed  by the store owner/admin |
|GET /sales/Fetch a single sale record	|This endpoint gets a specific sale record using the sale record Id. Accesed by the store owner/admin and the creator (store attendant) of the specific sale record.|
|POST /Create a product | This endpoint creates a new product record. Accessed by  the store owner/admin only.|
|PUT /Modify a product|This endpoint modifys a product details. Accessed by the Admin|
|Delete/Delete a product record order|This endpoint deletes a product from a products record. Accessed by th admin|
|POST /Create a user account|This endpoint creates a new user account.Accessed by the Admin|
|POST /Sign in to a use account|This signs in a user to their account.Accessed by admin and store attendant|

### How to run the application

- open a git bash
- git clone https://github.com/MbugwaSami/ADC2-Store-Manager-Api.git
- cd ADC3-Store-Manager-Api
- pip install virtualenv
- python -m venv venv
- source venv/scripts/activate
- pip install flask
- pip install flask-restful
- install postgresql
- python run.py
- Test the endpoints url on postaman


### How to run the tests 

- open a git bash
- git clone https://github.com/MbugwaSami/ADC2-Store-Manager-Api.git
- cd ADC2-Store-Manager-Api/
- pip install virtualenv
- python -m venv venv
- source venv/scripts/activate
- pip install flask
- pip install flask-restful
- pip install pytest
- pip install pylint
- install postgresql
- cd tests
- pytest test_product.py to run the products tests
- pytest test_sales.py to run the sales tests
- pytest test_auths.py to run the auth tests


