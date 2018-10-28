import unittest
import os
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
            email = "saminjau12@gmail.com",
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

		self.test_login = dict(
            email = "samiNjau@gmail.com",
            password = "Mwoboko10@",
            )

		self.test_login1 = dict(
            email = "njau.sammy@gmail.com",
            password = "Mwobok",
            )

		self.test_product =dict(
		    product_id = "r1",
            product_name = "khaki Trouser",
            description = "italian export",
			category = "clothes",
            price = 1000,
            stock = 100,
            minStock = 10
            )

		self.test_product1 =dict(
            product_id = "",
            product_name = "",
            description = "italian export",
		    category = "clothes",
            price = 1000,
            stock = 100,
            minStock = 10
           )

		self.test_product2 =dict(
           product_id = "r1",
           product_name = "khaki shirt",
           description = "italian export",
		   category = "clothes",
           price = 1000,
           stock = 100,
           minStock = 10
           )

		self.test_product3 =dict(
          product_id = "r34",
          product_name = "Legsin Trouser",
          description = "italian export",
		  category = "clothes",
          price = "sammy",
          stock = 100,
          minStock = 10
          )

		self.test_product4 =dict(
          product_id = "q3",
          product_name = "legsin shirt",
          description = "italian export",
	   	  category = "clothes",
          price = 1000,
          stock = 30.5,
          minStock = 10
          )

		self.test_product5 =dict(
          product_id = "t3",
          product_name = "AirForce shoe",
          description = "italian export",
		  category = "shoes",
          price = 1000,
          stock = 100,
          minStock = "sammmy"
          )
		self.test_product6 =dict(
          product_id = "t31",
          product_name = "Air max",
          description = "italian export",
		  category ="Shoes",
          price = 1000,
          stock = 100,
          minStock = 10
          )
