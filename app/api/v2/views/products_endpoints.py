from flask import Flask, jsonify, request
from flask_restful import Resource
from ..models.products import Products

products_object = Products()
class ProductsApi(Resource):
    """
    This class endpoints for products.
    """

    def post(self):
        """"
        This method posts data of a product.
        returns: json response.
        raises:product fields cannot be empty.
        raises:product name cannot be empty error.
        raises:price must be a number message.
        raises:stock must be an integer messager.
        """


        data=request.get_json()

        if not data:
            return {'message':'Products data cannot be empty'}

        product_id = data.get('product_id')
        product_name = data.get('product_name')
        description = data.get('description')
        category = data.get('category')
        price = data.get('price')
        stock = data.get('stock')
        minStock = data.get('minStock')

        response = jsonify(products_object.add_product(product_id,product_name,description,category,price,stock,minStock))
        response.status_code = 201

        return response
