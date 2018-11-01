from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)

from ..models.products import Products


class ProductsApi(Resource):
    """
    This class endpoints for products.
    """
    @jwt_required
    def post(self):
        """"
        This method posts data of a product.
        returns: json response.
        raises:product fields cannot be empty.
        raises:product name cannot be empty error.
        raises:price must be a number message.
        raises:stock must be an integer messager.
        """
        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return make_response(jsonify({'message':'You are not allowed to perform this action, contact the system admin!'}),401)

        data=request.get_json()

        if not data:
            return make_response(jsonify({'message':'Products data cannot be empty'}),200)


        product_name = data.get('product_name').lower()
        description = data.get('description')
        category = data.get('category')
        price = (data.get('price'))
        stock = (data.get('stock'))
        minStock = (data.get('minStock'))

        product1 = Products(product_name, description, category, price, stock, minStock)

        required_data = [product_name, description, category, price, stock, minStock]
        for field in required_data:
            if not field:
                return make_response(jsonify({"message": "Some required data fields are empty! only description and category can be empty"}),200)

        if product1.get_product_by_name():
            return dict(message = "This product is alrleady in the system")

        try:
            price = float(price)
        except ValueError:
            return make_response(jsonify({"message":"Product price can only be a number"}),200)


        if type((stock)) is not int:

            return make_response(jsonify({'message':'Stock can only be an integer'}),200)

        if type((minStock)) is not int:

            return make_response(jsonify({'message':'Minimum Stock can only be an integer'}),200)


        response = make_response(jsonify(product1.add_product()),201)


        return response

    @jwt_required
    def get(self):

        product3 = Products()
        """"
        This method gets data of all products.
        returns:items details
        """

        products = product3.get_products()
        if not products:
            return make_response(jsonify({"message":"no product available in the system"}),200)
        response = make_response(jsonify({"This are the available products":products}),200)
        return response

class SingleProductApi(Resource):
    """This is the class with get method for a single product"""
    @jwt_required
    def get(self,product_id):
        """
        This method gets data of a single product.
        returns: details of a single product.
        """
        product2 = Products()
        if not product2.get_product_by_id(product_id):
            return make_response(jsonify({"message":"product not available"}))

        response = make_response(jsonify(product2.get_product_by_id(product_id)),200)
        return response

    @jwt_required
    def delete(self,product_id):
            product3 = Products(product_id)
            claims = get_jwt_claims()
            if claims['role'] != "admin":
                return make_response(jsonify({'message':'You are not allowed to perform this action, contact the system admin!'}),401)
            response = make_response(jsonify(product3.delete_product(product_id)),200)

            return response

    @jwt_required
    def put(self,product_id):


        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return make_response(jsonify({'message':'You are not allowed to perform this action, contact the system admin!'}),401)

        data=request.get_json()

        description = data.get('description')
        category = data.get('category')
        price = (data.get('price'))
        stock = (data.get('stock'))
        minStock = (data.get('minStock'))
        product4 = Products(product_id,description,category,price,stock,minStock)


        product  = product4.get_product_by_id(product_id)
        if not product:
            return make_response(jsonify({"message":"This product is not in the system"}),200)
        if not category:
            category = product["category"]
        if not description:
            description = product["description"]
        if not price:
            price = product["price"]
        if not stock:
            qty = product["stock"]
        if not minStock:
            minStock=product["minStock"]

        response = make_response(jsonify(product4.update_product(product_id)),200)

        return response
