from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)

from ..models.sales import Sales
from ..models.products import Products


buyer_cart =[]
current_product = {}

class SalesApi(Resource):
    """This class has the post method to the sales database."""
    @jwt_required
    def post(self):
        """
        This method posts data of a sale.
        returns: json response.
        """




        sale = Sales(buyer_cart)
        sale.add_sale()





class SingleSalesApi(Resource):
    """
    This class endpoints for products.
    """
    @jwt_required
    def get(self,product_id,quantity):
        """
        This method posts data of a sale.
        returns: json response.
        """

        """
        This method gets data of a single product.
        returns: details of a single product.
        """

        product = Products()
        sale_product =product.get_product_by_id(product_id)
        if not sale_product:
            return make_response(jsonify({"message": "This product does not exist"}),200)

        elif   sale_product['stock'] == sale_product['min_stock']:
            return make_response(jsonify({"message": "The following product has reached the mimimum stock, please contact the admin for sales below minimum stock"}))
        elif   sale_product['stock'] == 0:
            return make_response(jsonify({"message": "This product is out of stock"}))

        claims = get_jwt_claims()
        current_product['product_name'] =sale_product['product_name']
        current_product['product_id'] =sale_product['product_id']
        current_product['price'] = sale_product['price']
        current_product['quantity'] = quantity
        current_product['subtotal'] = current_product['price']*quantity
        current_product['user_id'] = claims['user']
        buyer_cart.append(current_product)
        return make_response(jsonify({ "Buyers Cart":buyer_cart}))
