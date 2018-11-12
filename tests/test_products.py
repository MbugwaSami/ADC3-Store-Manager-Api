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

        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual("This product is alrleady in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)


        #test product two has been added
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_sale_product),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("jeans trouser succesfuly added",response_data["message"])
        self.assertEqual(response.status_code, 201)

        #test product data is not empty
    def test_product_data_not_empty(self):

        """This method tests wheather a product data is empty.
           :param1:client.
           :products data
           :returns:response:
        """
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
    def test_some_fields_not_empty(self):

        """This method tests wheather some product fields are empty.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product1),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Some required data fields are empty! only description and category can be empty",response_data["message"])
        self.assertEqual(response.status_code, 200)




        # test product price is a number
    def test_price_is_a_number(self):

        """This method tests wheather product price is number.
           :param1:client.
           :products data
           :returns:response:
        """
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
    def test_stock_is_an_integer(self):

        """This method tests wheather stock is an integer.
           :param1:client.
           :products data
           :returns:response:
        """
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
    def test_minStock_is_an_integer(self):

        """This method tests wheather a product price is an integer.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product5),
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("Minimum Stock can only be an integer",response_data["message"])
        self.assertEqual(response.status_code, 200)


    # get a single product by product code
    def test_get_one_product(self):

        """This method tests wheather a single retrieved.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/products/2',
        headers=dict(Authorization="Bearer " + self.owner_token))
        self.assertEqual(response.status_code, 200)


    #get all products
    def test_get_all_product(self):

        """This method tests wheather all products are retrived.
           :param1:client.
           :products data
           :returns:response:
        """
        # test admin can get all productds
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

        # test attendant can get all products
    def test_attendant_get_all_product(self):

        """This method tests wheather an attendant can retrive a product.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/products',
        headers=dict(Authorization="Bearer " + self.attendant_token),)
        response_data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)


    def test_modify_product(self):
        """This method tests the method for updating product details
           :param1:client.
           :products data
           :returns:response:
        """
        # check if updated item exists
        response = self.client.put(
        '/api/v2/products/8888',
        headers=dict(Authorization="Bearer " + self.owner_token),
        data = json.dumps(self.test_product),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual("This product is not in the system",response_data["message"])
        self.assertEqual(response.status_code, 200)

        response = self.client.put(
        '/api/v2/products/2',
        data = json.dumps(self.test_product7),
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

        response = self.client.delete(
        '/api/v2/products/1',
        headers=dict(Authorization="Bearer " + self.owner_token)
        )
        self.assertEqual(response.status_code, 200)


        response = self.client.get(
        '/api/v2/products/1',
        headers=dict(Authorization="Bearer " + self.owner_token))
        response_data = json.loads(response.data)
        self.assertEqual("product not available",response_data["message"])

    def test_attendant_cannot_add_a_product(self):
        """This method checks wheather an attendant cannot add a product.
           :test delete_product
           :test create products
           :test modify product
        """

        response = self.client.post(
        '/api/v2/products',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)

    def test_attendant_cannot_delete_a_product(self):

        """This method tests wheather an attendant cannot delete a productt.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.delete(
        '/api/v2/products/2',
        data = json.dumps(self.update_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)

    def test_attendant_cannot_update_a_product(self):

        """This method tests wheather an attendant cannot update a product.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.put(
        '/api/v2/products/2',
        data = json.dumps(self.test_product),
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"],"You are not allowed to perform this action, contact the system admin!")
        self.assertEqual(response.status_code, 401)
