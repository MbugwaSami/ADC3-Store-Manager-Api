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
        self.assertEqual("Some required data fields are empty! only description and category can be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test a product name is unique
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual("This product is alrleady in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test a product code is unique
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product2),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product id is alrleady used",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product price is a number
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product3),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product price can only be a number",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product stock is an integer
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product4),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Stock can only be an integer",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product mimimum stock is an integer
        response = self.client.post(
        '/api/v2/products',
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
        self.assertEqual("Air max succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/v2/products')
        self.assertEqual(response.status_code, 200)

        # get a single product by product code
        response = self.client.get('/api/v2/products/t31')
        self.assertEqual(response.status_code, 200)

    def test_modify_product(self):
        """This method tests the method for updating product details
           :param1:client.
           :products data
           :returns:response:
        """
        # check if updated item exists
        response = self.client.put(
        '/api/v2/products/t3oo1',
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product is not in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)

        response = self.client.put(
        '/api/v2/products/t31',
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        """This method tests the method for deleting a product.
           :param1:client.
           :products data
           :returns:response:
        """

        response = self.client.delete(
        '/api/v2/products/r1',
        data = json.dumps(self.update_product),
        content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)


        response = self.client.get('/api/v2/products/r1')
        response_data = json.loads(response.data)
        self.assertEqual("product not available",response_data["message"])
