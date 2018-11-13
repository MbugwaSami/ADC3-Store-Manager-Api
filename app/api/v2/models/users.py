from werkzeug.security import generate_password_hash, check_password_hash
import re
from psycopg2.extras import RealDictCursor
import psycopg2
import os
from instance.config import app_config



enviroment = os.environ['ENVIRONMENT']
class Users():
    """
    This class has methods for manipulation of user data.
    """
    def __init__(self,email =None,names =None,password= None,role =None):
        self.email = email
        self.names = names
        self.password = password
        self.role = role
        self.conn = psycopg2.connect(app_config[enviroment].connectionVariables)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)



    # method to add new user
    def add_user(self):
        """"
        This method adds anew user
        param1:email
        param2:names.
        paeram3:password.
        param4:role.

        returns: user added messages.
        """
        password = generate_password_hash(self.password)
        self.cur.execute("INSERT INTO users(email,names, password,role) VALUES(%s,%s,%s,%s)",
        (self.email,self.names,password,self.role))
        self.conn.commit()

        return {'message':"User account succesfuly created"}

    def get_one_user(self):
        """This method gets one user from the database
           :param1:email.
           :returns:user.
        """

        self.cur.execute("SELECT user_id,email,names,role FROM users where email =%s",(self.email,))
        return self.cur.fetchone()

    def get_all_users(self):
        """
        This method gets all details users
        returns:all_users
        """
        self.cur.execute("SELECT user_id, email,names,role FROM users")
        return self.cur.fetchall()

    def verify_user(self):
        """This method verifys user  details during login.
           :param1:email.
           :param2:password.
        """
        try:
            self.cur.execute("SELECT  password FROM users WHERE email = %s ",(self.email,))
        except Exception as a:
            self.cur.close()
            self.conn.close()
        result=self.cur.fetchone()
        if not result:
            return False
        valid_login = check_password_hash(result["password"], self.password)
        return valid_login




    def validate_password(self):
        """
        This method checks for strength of a password.
        :return:password is valid or not.
        """
        is_password_valid = True
        if (len(self.password)<6 or len(self.password)>12):
            is_password_valid = False
        elif not re.search("[a-z]",self.password):
            is_password_valid = False
        elif not re.search("[A-Z]",self.password):
            is_password_valid = False
        elif not re.search("[0-9]",self.password):
            is_password_valid = False
        elif not re.search("[$#@]",self.password):
            is_password_valid = False
        return is_password_valid

    def validate_email(self):
        """This method checks wheather an email is validate.
           :param:email.
           :returns: email is valid or not.
        """
        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email,re.IGNORECASE):
            return True
        return False

    def blacklist_token(self,json_token):

        try:
            self.cur.execute("INSERT INTO blacklist(json_token) VALUES(%s)",(json_token,))
            self.conn.commit()

        except Exception as e:
            self.cur.close()
            self.conn.close()

    def check_blacklist(self,json_token):

        try:
            self.cur.execute("SELECT * FROM blacklist WHERE json_token = %s",(json_token,))
            return self.cur.fetchone()
        except Exception as e:
            raise
