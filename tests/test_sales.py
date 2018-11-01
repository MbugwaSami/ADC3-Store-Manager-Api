import json

from .base_test import TestBase

class TestProducts(TestBase):
    """This class has methods that test methods used in manipulation of sale data."""

    def test_add_to_cart(self):

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']
        # test create user
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

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(dict(
        email = "saminjau12@gmail.com",
        password = "Mfhry45978#",

        )),
        content_type = 'application/json'
        )
        self.attendant_token = json.loads(response.data.decode())['token']

        # test sale products not in db

        response = self.client.get(
        '/api/v2/sales/add/1w',
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"This product does not exist")
        self.assertEqual(response.status_code,200)

        # test add item in sytem

        response = self.client.get(
        '/api/v2/sales/add/r45',
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"The following product has reached the mimimum stock, please contact the admin for sales below minimum stock")
        self.assertEqual(response.status_code,200)

        # test sale item at zero stock

        response = self.client.get(
        '/api/v2/sales/add/r',
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"This product is out of stock")
        self.assertEqual(response.status_code,200)

        # test sale item at lower limit

        response = self.client.get(
        '/api/v2/sales/add/r1',
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"Item added to cart")
        self.assertEqual(response.status_code,200)
