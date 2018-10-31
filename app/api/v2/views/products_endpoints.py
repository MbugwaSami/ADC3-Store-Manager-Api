from flask import Flask, jsonify, request
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)

from ..models.products import Products

products_object = Products()
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
            return jsonify({'message':'You are not allowed to perform this action, contact the system admin!'})

        data=request.get_json()

        if not data:
            return {'message':'Products data cannot be empty'}

        product_id = data.get('product_id').lower()
        product_name = data.get('product_name').lower()
        description = data.get('description')
        category = data.get('category')
        price = (data.get('price'))
        stock = (data.get('stock'))
        minStock = (data.get('minStock'))

        required_data = [product_id, product_name, description, category, price, stock, minStock]
        for field in required_data:
            if not field:
                return dict(message = "Some required data fields are empty! only description and category can be empty")

        if products_object.get_one_product(product_name):
            return dict(message = "This product is alrleady in the system")

        if products_object.get_one_product(product_id):
            return dict(message = "This product id is alrleady used")
        try:
            price = float(price)
        except ValueError:
            return dict(message = "Product price can only be a number")


        if type((stock)) is not int:

            return {'message':'Stock can only be an integer'}

        if type((minStock)) is not int:

            return {'message':'Minimum Stock can only be an integer'}


        response = jsonify(products_object.add_product(product_id,product_name,description,category,price,stock,minStock))
        response.status_code = 201

        return response

    @jwt_required
    def get(self):

        """"
        This method gets data of all products.
        returns:items details
        """
        response = jsonify(products_object.get_products())
        response.status_code = 200
        return response

class SingleProductApi(Resource):
    """This is the class with get method for a single product"""
    @jwt_required
    def get(self,product_id):
        """
        This method gets data of a single product.
        returns: details of a single product.
        """
        if not products_object.get_one_product(product_id):
            return dict(message = "product not available")

        response = jsonify(products_object.get_one_product(product_id))
        response.status_code = 200
        return response
    @jwt_required

    def delete(self,product_id):

            claims = get_jwt_claims()
            if claims['role'] != "admin":
                return jsonify({'message':'You are not allowed to perform this action, contact the system admin!'})
            response = jsonify(products_object.delete_product(product_id))
            response.status_code = 200

            return response

    @jwt_required
    def put(self,product_id):

        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return jsonify({'message':'You are not allowed to perform this action, contact the system admin!'})

        data=request.get_json()

        description = data.get('description')
        category = data.get('category')
        price = (data.get('price'))
        stock = (data.get('stock'))
        minStock = (data.get('minStock'))


        product  = products_object.get_one_product(product_id)
        if not product:
            return jsonify(dict(message = "This product is not in the system"))
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

        response = jsonify(products_object.update_product(description,category,price,stock,minStock))
        response.status_code = 200

        return response
