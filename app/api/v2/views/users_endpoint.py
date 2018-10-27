from flask import Flask, jsonify, request
from flask_restful import Resource

from ..models.users import Users


user_object=Users()
# endpoin for creating user

class UsersApi(Resource):
    """
    This class has post and get method of all users.
    """

    def post(self):
        """"
        This method posts data of a user.
        returns: json response.



        """
        data=request.get_json()

        if not data:
            return {'message':'Fields cannot be empty'}
        email = data.get('email')
        names = data.get('names')
        password = data.get('password')
        role = data.get('role')

        response = jsonify(user_object.add_user(email,names,password,role))
        response.status_code = 201
        return response
