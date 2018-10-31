import json

from .base_test import TestBase

class TestProducts(TestBase):
    """This class has methods that test methods used in manipulation of product data."""

    def test_add_product(self):

        """This method tests wheather a product has been added.
           :param1:client.
           :products data
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']

        #test product has been added
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("khaki trouser succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)


        #test product data is not empty
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps({}),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Products data cannot be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)

        #test non empty data fields
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product1),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Some required data fields are empty! only description and category can be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test a product name is unique
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual("This product is alrleady in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test a product code is unique
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product2),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product id is alrleady used",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product price is a number
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product3),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Product price can only be a number",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product stock is an integer
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product4),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Stock can only be an integer",response_data["message"])
        self.assertEqual(response.status_code, 200)

        # test product mimimum stock is an integer
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product5),
        headers=dict(Authorization="Bearer " + self.owner_token),
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
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']
        #get all products
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product6),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("air max succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)

        response = self.client.get(
        '/api/v2/products',
        headers=dict(Authorization="Bearer " + self.owner_token),)
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        

        # get a single product by product code
        response = self.client.get(
        '/api/v2/products/t31',
        headers=dict(Authorization="Bearer " + self.owner_token),)
        self.assertEqual(response.status_code, 200)

    def test_modify_product(self):
        """This method tests the method for updating product details
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']
        # check if updated item exists
        response = self.client.put(
        '/api/v2/products/t3oo1',
        headers=dict(Authorization="Bearer " + self.owner_token),
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product is not in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)

        response = self.client.put(
        '/api/v2/products/t31',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        """This method tests the method for deleting a product.
           :param1:client.
           :products data
           :returns:response:
        """

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']

        response = self.client.delete(
        '/api/v2/products/r1',
        data = json.dumps(self.update_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )
        self.assertEqual(response.status_code, 200)


        response = self.client.get(
        '/api/v2/products/r1',
        headers=dict(Authorization="Bearer " + self.owner_token))
        response_data = json.loads(response.data)
        self.assertEqual("product not available",response_data["message"])

    def test_unauthorized_actions(self):
        """This method checks wheather a user can perform unauthorized actions.
           :test delete_product
           :test create products
           :test modify product
        """

        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.owner_login),
        content_type = 'application/json'
        )
        self.owner_token = json.loads(response.data.decode())['token']
        # create attendant account
        response = self.client.post(
        '/api/v2/users',
        data = json.dumps(self.test_user7),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"User account succesfuly created")
        self.assertEqual(response.status_code, 201)

        # login a normal user
        response = self.client.post(
        '/api/v2/users/login',
        data = json.dumps(self.test_login2),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.attendant_token = json.loads(response.data.decode())['token']
        self.assertEqual(response_data["message"],"wellcome SAMMY NJAU, you are loged in as attendant")
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)

        response = self.client.delete(
        '/api/v2/products/r1',
        data = json.dumps(self.update_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)


        response = self.client.put(
        '/api/v2/products/t31',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)
