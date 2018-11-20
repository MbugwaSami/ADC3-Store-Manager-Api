import unittest
import os
import json
from app import create_app
from instance.config import app_config
from connection import DbBase
db = DbBase()
class TestBase(unittest.TestCase):
	"""This class holds data shared among tests"""
	db.dropTables()
	def setUp(self):
		"""The setUp method is the method that initialize the variables to be used by the test methods"""

		config="testing"
		self.app = create_app(config)
		self.client = self.app.test_client()
		self.app_context = self.app.app_context()


		self.test_user = dict(
		email = "samiNjau@gmail.com",
		names = "Sammy Njau",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.test_user1 = dict(
		email = "mbugwa@gmail.com",
		names = "Sammy Njau",
		password = "Mwoboko10@",
		role = "attendant",
		)



		self.test_user2 = dict(
		email = "saminjeri@gmailcom",
		names = "Sammy Njau",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.test_user3 = dict(
		email = "sami.njau12@gmail.com",
		names = "Sammy Njau",
		password = "111",
		role = "attendant",
		)

		self.test_user4 = dict(
		email = "sami.mbugwa@gmail.com",
		names = "Sammy Njau",
		password = "Mwoboko10@",
		role = "customer",
		)

		self.test_user5 = dict(
		email = "sami.mbugwa@gmail.com",
		names = "",
		password = "Mwoboko10@",
		role = "admin",
		)

		self.test_user6 = dict(
		email = "njau.sammy@gmail.com",
		names = "sammy njau",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.test_user7 = dict(
		email = "sammy@gmail.com",
		names = "sammy njau",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.test_user8 = dict(
		email = "sammy@gmail.com",
		names = "sammy mbugua",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.login_user = dict(
		email = "sammy@gmail.com",
		names = "sammy mbugua",
		password = "Mwoboko10@",
		role = "attendant",
		)

		self.test_login = dict(
		email = "sammy@gmail.com",
		password = "Mwoboko10@",
		)

		self.test_login1 = dict(
		email = "njau.sammyl.com",
		password = "Mwobok",
		)

		self.test_login2 = dict(
		email = "sammy@gmail.com",
		password = "Mwoboko10@",
		)

		self.owner_login = dict(
		email = "admin@quickwear.com",
		password = "@Admin1",
		)


		self.owner_login1 = dict(
		email = "sam@gmai.com",
		password = "Sammy10@",
		)

		self.test_sale_product =dict(
		product_name = "Jeans Trouser",
		description = "italian export",
		category = "clothes",
		price = 1000,
		stock = 100,
		minStock = 10
		)

		self.test_product =dict(
		product_name = "khaki Trouser",
		description = "italian export",
		category = "clothes",
		price = 1000,
		stock = 100,
		minStock = 10
		)

		self.test_product1 =dict(
		product_name = "",
		description = "italian export",
		category = "clothes",
		price = 1000,
		stock = 100,
		minStock = 10
		)

		self.test_product2 =dict(
		product_name = "khaki shirt",
		description = "italian export",
		category = "clothes",
		price = 1000,
		stock = 100,
		minStock = 10
		)

		self.test_product3 =dict(
		product_name = "Legsin Trouser",
		description = "italian export",
		category = "clothes",
		price = "sammy",
		stock = 100,
		minStock = 10
		)

		self.test_product4 =dict(
		product_name = "legsin shirt",
		description = "italian export",
		category = "clothes",
		price = 1000,
		stock = "uuu",
		minStock = 10
		)

		self.test_product5 =dict(
		product_name = "AirForce shoe",
		description = "italian export",
		category = "shoes",
		price = 1000,
		stock = 100,
		minStock = "sammmy"
		)
		self.test_product6 =dict(
		product_name = "Air max",
		description = "italian export",
		category ="Shoes",
		price = 1000,
		stock = 100,
		minStock = 10
		)

		self.test_product7 =dict(
		description = "italian export",
		category ="clothes",
		price = 1000,
		stock = 100,
		minStock = 100
		)


		self.update_product =dict(
		description = "france origin",
		category ="Shoes",
		price = 1500,
		stock = 80,
		minStock = 10
		)

		response = self.client.post(
		'/api/v2/users/login',
		data = json.dumps(self.owner_login),
		content_type = 'application/json'
		)
		self.owner_token = json.loads(response.data.decode())['token']

		# create an attendant

		response = self.client.post(
		'/api/v2/users',
		data = json.dumps(dict(
		email = "saminjau12@gmail.com",
		names = "Sammy Njau",
		password = "Mfhry45978#",
		role = "attendant",
		)),
		headers=dict(Authorization="Bearer " + self.owner_token),
		content_type = 'application/json'
		)

		#login the attendant
		response = self.client.post(
		'/api/v2/users/login',
		data = json.dumps(dict(
		email = "saminjau12@gmail.com",
		password = "Mfhry45978#",
		)),
		content_type = 'application/json'
		)

		self.attendant_token = json.loads(response.data.decode())['token']
