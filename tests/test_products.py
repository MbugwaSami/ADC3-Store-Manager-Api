import json

from tests import TestBase

class TestProducts(TestBase):
    """This class has methods that test methods used in manipulation of product data."""

    def test_add_product(self):

        """This method tests wheather a product has been added.
           :param1:client.
           :products data
           :returns:response:
        """
        #test product has been added
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("khaki Trouser succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)

        #test product data is not empty
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps({}),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Products data cannot be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)

        #test non empty data fields
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product1),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Some data fields are empty!",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test a product name is unique
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )

        # test a product code is unique
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_prouduct2),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product is alrleady in the system",response_data["message"])
        self.assertEqual(response.status_code, 201)

        # test product price is a number
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_product3),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product price can only be a number",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product stock is an integer
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_product4),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Stock can only be an integer",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product mimimum stock is an integer
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_product5),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Minimum Stock can only be an integer",response_data["message"])
        self.assertEqual(response.status_code, 200)



    def test_get_product(self):

        """This method tests wheather all products are  retrieved.
           :param1:client.
           :products data
           :returns:response:
        """
        #get all products
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product6),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 200)

        # get a single product by product code
        response = self.client.get('/api/v2/products/t31')

        response_data = json.loads(response.data)
        self.assertEqual("Air Max was found",response_data["message"])
        self.assertEqual(response.status_code, 201)
