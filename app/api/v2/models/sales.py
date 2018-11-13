from psycopg2.extras import RealDictCursor
import psycopg2
import os
from instance.config import app_config



enviroment = os.environ['ENVIRONMENT']
class Sales():
    """
    This class has methods for manipulation of products data.
    """
    def __init__(self,buyer_cart = None, totals =None):
        self.buyer_cart = buyer_cart
        self.totals = totals
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
        self.cur.execute("""INSERT INTO transactions(total,product_count,user_id)
        VALUES(%s,%s,%s) RETURNING sale_id;""",(self.totals[0],self.totals[1],self.totals[2]))
        sale_id = self.cur.fetchone()["sale_id"]
        for item in self.buyer_cart:
            item.update( {'sale_id' : sale_id} )
        print(self.buyer_cart)
        self.cur.executemany("""INSERT INTO sales(product_name,quantity,subtotal,sale_id)
        VALUES(%(product_name)s,%(quantity)s,%(subtotal)s,%(sale_id)s)""",
        self.buyer_cart)
        self.conn.commit()
        self.cur.executemany("UPDATE products set stock = stock - %(quantity)s where product_id = %(product_id)s",self.buyer_cart)
        self.conn.commit()

    def get_all_sales(self):
          try:
              self.cur.execute("SELECT * FROM sales INNER JOIN transactions ON sales.sale_id = transactions.sale_id")
              sales = self.cur.fetchall()
              return sales
          except Exception as e:
              self.cur.close()
              self.conn.close()

    def get_sales_by_user(self,user_id):
            self.cur.execute("""SELECT * FROM sales INNER JOIN transactions ON sales.sale_id = transactions.sale_id
             WHERE user_id = %s""",(user_id,))
            return self.cur.fetchall()



    def get_sales_by_id(self,sale_id):
              self.cur.execute("SELECT * FROM  sales WHERE user_id = %s",(user_id,))
              sales = self.cur.fetchall()
              return sales
