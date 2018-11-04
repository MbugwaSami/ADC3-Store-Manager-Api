import json

from .base_test import TestBase

class TestSales(TestBase):
    """This class has methods that test methods used in manipulation of sale data."""

    #test admin cannot add item
    def test_admin_cannot_add_item(self):

        """This method tests wheather an admim cannot add an item to the cart.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/sales/3/2',
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"You cannot make a sale from an Admin account, Consider having an attendant account")
        self.assertEqual(response.status_code,401)

    #test admin cannot sale
    def test_admin_cannot_post_sale(self):

        """This method tests wheather an admin cannot post sale from admin account.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/sales',
        headers=dict(Authorization="Bearer " + self.owner_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"You cannot make a sale from an Admin account, Consider having an attendant account")
        self.assertEqual(response.status_code,401)


    def test_add_to_cart_item_not_in_system(self):

        """This method tests wheather a product to be sold is not in the sysytem.
           :param1:client.
           :products data
           :returns:response:
        """
        # test sale products not in db

        response = self.client.get(
        '/api/v2/sales/1999/2',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )

        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"This product does not exist")
        self.assertEqual(response.status_code,200)


        # test add item which is at minimum stock
    def test_add_to_cart_item_at_minimum_stock(self):

        """This method tests wheather a product to be sold has reached minimum stock.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/sales/2/1',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"The following product has reached the mimimum stock, please contact the admin for sales below minimum stock")
        self.assertEqual(response.status_code,200)

    # test add to cart
    def test_add_to_cart(self):

        """This method tests wheather a product can be added to the cart.
           :param1:client.
           :products data
           :returns:response:
        """
        # test empty cart
        response = self.client.post(
        '/api/v2/sales',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"please add an item to cart")
        self.assertEqual(response.status_code,200)

        # test sale item that can be sold
        response = self.client.get(
        '/api/v2/sales/3/2',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"This are the items on your Cart")
        self.assertEqual(response.status_code,200)


    # test post a sale
    def test_get_post_a_sale(self):

        """This method tests wheather a sale has been posted.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.post(
        '/api/v2/sales',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"your sale was succesful")
        self.assertEqual(response.status_code,200)

        #test sale was succesful
        response = self.client.get(
        '/api/v2/sales/2',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"This are your sales")
        self.assertEqual(response.status_code,200)




    # test get sales for another user
    def test_cannot_get_other_attendant_sales(self):

        """This method tests wheather an attendant can get another attendant sales.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/sales/1',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"You can only view your sales")
        self.assertEqual(response.status_code,401)

    # test attendant cannot view all sales
    def test_attendant_cannot_view_all_sales(self):

        """This method tests wheather attendant cannot view all sales.
           :param1:client.
           :products data
           :returns:response:
        """
        response = self.client.get(
        '/api/v2/sales',
        headers=dict(Authorization="Bearer " + self.attendant_token),
        content_type = 'application/json'
        )
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'],"You dont have rights to list all sales, contact the system admin")
        self.assertEqual(response.status_code,401)
