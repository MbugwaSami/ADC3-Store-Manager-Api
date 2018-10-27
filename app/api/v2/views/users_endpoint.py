from flask import Flask, jsonify, request
from flask_restful import Resource
from connection import DbBase
from ..models.users import Users


user_object=Users()
# endpoin for creating user
db=DbBase()
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

        email = data.get('email').lower()
        names = data.get('names').upper()
        password = data.get('password')
        role = data.get('role').lower()

        user_details = [email,names,password,role]

        for field in user_details:
            if not field or field.isspace():
                return {'message':'Some fields are empty!'}

        if not user_object.validate_email(email):
            return {'message':'Please enter a valaid email'}

        if user_object.get_one_user(email):
            return {'message':'User account alrleady exists'}

        if not (role == "admin" or role == "attendant"):
            return {'message':'Roles can only be admin or attendant'}

        if not user_object.validate_password(password):
            return {'message':'password should be between 6 and 12 characters, have atleast one lower_case,'+
            'one Upper_case,one number and one special character'}

        response = jsonify(user_object.add_user(email,names,password,role))
        response.status_code = 201
        return response
