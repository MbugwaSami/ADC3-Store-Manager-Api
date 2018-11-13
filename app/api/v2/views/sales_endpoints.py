from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)

from ..models.sales import Sales
from ..models.products import Products


buyer_cart = []


class SalesApi(Resource):
    """This class has the post method to the sales database."""
    @jwt_required
    def post(self):
        """
        This method posts data of a sale.
        returns: json response.
        """

        claims = get_jwt_claims()
        if claims['role'] != "attendant":
            return make_response(jsonify({'message':'You cannot make a sale from an Admin account, Consider having an attendant account'}),401)

        if len(buyer_cart) == 0:
            return make_response(jsonify({"message":"please add an item to cart"}))
        sale = Sales(buyer_cart)
        sale.add_sale()
        buyer_cart.clear()
        return make_response(jsonify({"message":"your sale was succesful"}))

    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return make_response(jsonify({'message':'You dont have rights to list all sales, contact the system admin'}),401)


        sale = Sales()
        sales = sale.get_all_sales()
        if not sales:
            return make_response(jsonify({"message":"No sales are available"}))
        return make_response(jsonify(sales))




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
        claims = get_jwt_claims()
        if claims['role'] != "attendant":
            return make_response(jsonify({'message':'You cannot make a sale from an Admin account, Consider having an attendant account'}),401)


        product = Products()
        sale_product =product.get_product_by_id(product_id)
        if not sale_product:
            return make_response(jsonify({"message": "This product does not exist"}),200)

        elif   sale_product['stock'] == sale_product['min_stock']:
            return make_response(jsonify({"message": "The following product has reached the mimimum stock, please contact the admin for sales below minimum stock"}))
        elif   sale_product['stock'] == 0:
            return make_response(jsonify({"message": "This product is out of stock"}))

        claims = get_jwt_claims()
        current_product ={
        "product_name": sale_product['product_name'],
        "product_id":  sale_product['product_id'],
        "price": sale_product['price'],
        "quantity": quantity,
        "subtotal": sale_product['price']*quantity,
        "user_id": claims['user']
        }
        buyer_cart.append(current_product)
        total = 0
        for item in buyer_cart:
            total = total + item['subtotal']
        return make_response(jsonify({ "buyers_cart":buyer_cart,"message":"This are the items on your Cart", "total":total}))

class SalesApiUser(Resource):
    """This class has the post method to the sales database."""


    @jwt_required
    def get(self,user_id):
        claims = get_jwt_claims()
        if not (claims['user'] == user_id or claims['role'] =="admin"):
            return make_response(jsonify({'message':'You can only view your sales'}),401)

        user_id =str(user_id)
        sale = Sales()
        sales = sale.get_sales_by_user(user_id)
        print(user_id)
        if not sales:
            return make_response(jsonify({"message":"No sales are available"}))
        return make_response(jsonify({"message":"This are your sales","sales":sales}),200)

class SalesApiSale(Resource):
    """This class has the post method to the sales database."""


    @jwt_required
    def get(self,sale_id):
        user_id =str(user_id)
        sale = Sales()
        sales = sale.get_sales_by_user(sale_id)
        if not sales:
            return make_response(jsonify({"message":"No sales are available"}))
        return make_response(jsonify(sales))
