from flask import Flask, jsonify, request
from flask_restful import Resource
from app import create_app
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)
from ..models.users import Users



user_object=Users()
class UsersApi(Resource):
    """
    This class has post and get method of all users.
    """
    @jwt_required
    def post(self):
        """"
        This method posts data of a user.
        returns: json response.



        """
        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return jsonify({'message':'You are not allowed to perform this action, contact the system admin!'})

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
                return jsonify({'message':'Some fields are empty!'})

        if not user_object.validate_email(email):
            return jsonify({'message':'Please enter a valaid email'})

        if user_object.get_one_user(email):
            return {'message':'User account alrleady exists'}

        if not (role == "admin" or role == "attendant"):
            return jsonify({'message':'Roles can only be admin or attendant'})

        if not user_object.validate_password(password):
            return jsonify({'message':'password should be between 6 and 12 characters, have atleast one lower_case,'+
            'one Upper_case,one number and one special character'})
        response = jsonify(user_object.add_user(email,names,password,role))
        response.status_code = 201
        return response
    @jwt_required
    def get(self):
        """
        This method gets data of all users.
        returns:Details of a users.
        """

        users = user_object.get_all_users()

        response = jsonify({"This are users in the system":users})
        response.status_code = 200

        return response

class SingleUserApi(Resource):
    """
    This class has post and get methods for single user data.
    """

    def post(self):
        """This method posts user data for a login"""

        data=request.get_json()

        if not data:
            return {'message':'please enter data to login'}
        email = data.get('email').lower()
        password = data.get('password')

        if not user_object.verify_user(email,password):
            return jsonify(dict(message = "wrong email or password"))
        logged_user = user_object.get_one_user(email)
        names = logged_user["names"]
        role = logged_user["role"]
        access_token = create_access_token(identity = logged_user)
        response = jsonify(dict(token = access_token, message = "wellcome "+names +", "+"you are loged in as "+role))
        response.status_code = 200
        return response
