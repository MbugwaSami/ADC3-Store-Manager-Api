from werkzeug.security import generate_password_hash
import re

from ..models import Models

enviroment="development"
class Users(Models):
    """
    This class has methods for manipulation of user data.
    """

    # method to add new user
    def add_user(self,email,names,password,role):
        """"
        This method adds anew user
        param1:email
        param2:names.
        paeram3:password.
        param4:role.

        returns: user added messages.
        """
        password = generate_password_hash(password)
        self.cur.execute("INSERT INTO users(email,names, password,role) VALUES(%s,%s,%s,%s)",
        (email,names,password,role))
        self.conn.commit()

        return {'message':"User account succesfuly created"}

    def get_one_user(self,email):
        """This method gets one user from the database
           :param1:email.
           :returns:user.
        """

        self.cur.execute("SELECT email,names,role FROM users where email =%s",(email,))
        return self.cur.fetchone()

    def get_all_users(self):
        """
        This method gets all details users
        returns:all_users
        """
        self.cur.execute("SELECT email,names,role FROM users")
        return self.cur.fetchall()

    def validate_password(self,password):
        """
        This method checks for strength of a password.
        :return:password is valid or not.
        """
        is_password_valid = True
        if (len(password)<6 or len(password)>12):
            is_password_valid = False
        elif not re.search("[a-z]",password):
            is_password_valid = False
        elif not re.search("[A-Z]",password):
            is_password_valid = False
        elif not re.search("[0-9]",password):
            is_password_valid = False
        elif not re.search("[$#@]",password):
            is_password_valid = False
        return is_password_valid

    def validate_email(self,email):
        """This method checks wheather an email is validate.
           :param:email.
           :returns: email is valid or not.
        """
        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email,re.IGNORECASE):
            return True
        return False
