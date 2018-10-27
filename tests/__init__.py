import unittest
import os
from app import create_app
from instance.config import app_config
from connection import DbBase
db = DbBase()
class TestBase(unittest.TestCase):
	""""""

	def setUp(self):
		config="testing"
		enviroment = os.environ['ENVIRONMENT']
		print(enviroment)
		self.app = create_app(config)
		self.client = self.app.test_client()

		self.test_user = dict(
            email = "samimbugwa@gmail.com",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "attendant",
            )


		self.test_user1 = dict(
            email = "samimbugwa@gmailcom",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "attendant",
            )

		self.test_user2 = dict(
            email = "samimbugwa@gmailcom",
            names = "Sammy Njau",
            password = "111",
            role = "attendant",
            )

		self.test_user3 = dict(
            email = "samimbugwa@gmailcom",
            names = "Sammy Njau",
            password = "111",
            role = "attendant",
            )

	def tearDown(self):

		db.dropTables()
