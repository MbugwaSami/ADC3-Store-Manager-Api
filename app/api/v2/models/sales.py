from psycopg2.extras import RealDictCursor
import psycopg2
import os
from instance.config import app_config



enviroment = os.environ['ENVIRONMENT']
class Sales():
    """
    This class has methods for manipulation of products data.
    """
    def __init__(self,buyer_cart):
        self.buyer_cart = buyer_cart
        self.conn = psycopg2.connect(app_config[enviroment].connectionVariables)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def add_sale(self):

        """"
        This method adds anew user
        param1:email
        param2:names.
        paeram3:password.
        param4:role.

        returns: user added messages.
        """

        try:
            self.cur.executemany("""INSERT INTO sales(product_name,quantity,subtotal,user_id)
             VALUES(%(product_name)s,%(quantity)s,%(subtotal)s,%(user_id)s)""",
            self.buyer_cart)
            self.conn.commit()
            self.cur.executemany("UPDATE products set stock = stock - %(quantity)s where product_id = %(product_id)s",self.buyer_cart)
            self.conn.commit()
        except Exception as e:
            self.cur.close()
            self.conn.close()
