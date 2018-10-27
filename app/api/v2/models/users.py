from werkzeug.security import generate_password_hash
from flask import current_app
from ..models import Models



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
        raises:invalid email message.
        raises:email alrleady added message.
        raises:invalid role message.
        raises:week password error.
        """
        password = generate_password_hash(password)
        self.cur.execute("INSERT INTO users(names,email, password,role) VALUES(%s,%s,%s,%s)",
        (email,names,password,role))
        self.conn.commit()

        return {'message':"User account succesfuly created"}

    def select_one_user(self,email):
        pass
