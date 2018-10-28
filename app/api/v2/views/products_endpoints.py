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

    def get(self,product_id):
        """
        This method gets data of a single product.
        returns: details of a single product.
        """

        response = jsonify(products_object.get_one_product(product_id))
        response.status_code = 200
        return response
