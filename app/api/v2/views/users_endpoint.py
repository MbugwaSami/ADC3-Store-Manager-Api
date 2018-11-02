
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource
from app import create_app
from datetime import datetime as dt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_claims)
from ..models.users import Users



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
            return make_response(jsonify({'message':'You are not allowed to perform this action, contact the system admin!'}),401)

        data=request.get_json()
        if not data:
            return {'message':'Fields cannot be empty'}

        email = data.get('email').lower()
        names = data.get('names').upper()
        password = data.get('password')
        role = data.get('role').lower()
        user1 = Users(email,names,password,role)
        user_details = [email,names,password,role]
        for field in user_details:
            if not field or field.isspace():
                return make_response(jsonify({'message':'Some fields are empty!'}),200)

        if not user1.validate_email():
            return make_response(jsonify({'message':'Please enter a valid email'}),200)

        if user1.get_one_user():
            return make_response(jsonify({'message':'User account alrleady exists'}),200)

        if not (role == "admin" or role == "attendant"):
            return make_response(jsonify({'message':'Roles can only be admin or attendant'}),200)

        if not user1.validate_password():
            return make_response(jsonify({'message':'password should be between 6 and 12 characters, have atleast one lower_case,'+
            'one Upper_case,one number and one special character'}),200)
        response = make_response(jsonify(user1.add_user()),201)
        return response
    @jwt_required
    def get(self):
        """
        This method gets data of all users.
        returns:Details of a users.
        """
        claims = get_jwt_claims()
        if claims['role'] != "admin":
            return make_response(jsonify({'message':'You are not allowed to perform this action, contact the system admin!'}),401)

        user1 = Users()
        users = user1.get_all_users()
        if not users:
            return make_response(jsonify({"There are no users in the system":users}),200)
        response = make_response(jsonify({"This are users in the system":users}),200)


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
        user2 = Users(email,password)
        if not user2.verify_user():
            return make_response(jsonify({"message": "wrong email or password"}),401)
        logged_user = user2.get_one_user()
        names = logged_user["names"]
        role = logged_user["role"]
        access_token = create_access_token(identity = logged_user)
        response = make_response(jsonify(dict(token = access_token, message = "wellcome "+names +", "+"you are loged in as "+role)),201)
        return response
