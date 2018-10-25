import unittest

from app import create_app
from instance.config import app_config

class TestBase(unittest.TestCase):
	""""""

	def setUp(self):
		config="testing"
		self.app = create_app(config)
		self.client = self.app.test_client()

		self.test_user = dict(
            email = "samimbugwa@gmail.com",
            names = "Sammy Njau",
            password = "Mwoboko10@",
            role = "attendant",
            ) 

