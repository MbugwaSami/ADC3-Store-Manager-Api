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
