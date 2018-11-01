from .base_model import Models

from psycopg2.extras import RealDictCursor
import psycopg2
import os
from instance.config import app_config


enviroment = os.environ['ENVIRONMENT']

class Products():
    """
    This class has methods for manipulation of products data.
    """

    def __init__(self,product_id = None, product_name = None ,description = None ,category = None ,price = None ,stock = None ,minStock = None):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.category = category
        self.price  = price
        self.stock  = stock
        self.minStock = minStock
        self.conn = psycopg2.connect(app_config[enviroment].connectionVariables)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)




    def add_product(self):
        """
        This method adds new product.
        param1:produ_id
        param2:product_name.
        paeram3:price.
        param4:stock.
        param5:minStock.

        returns: product added message.
        raises:product existing message.
        """

        try:
            self.cur.execute("INSERT INTO products(product_name,description,category,price,stock,min_stock)"+
            "VALUES(%s,%s,%s,%s,%s,%s)", (self.product_name,self.description,self.category,self.price,self.stock,self.minStock,))
            self.conn.commit()
        except Exception as e:
            self.cur.close
            self.conn.close

        return dict(message = self.product_name+" succesfuly added")

    def get_product_by_name(self):
        """This method check wheather a product is in the system.
           :param:product_id/product_name.
        """
        try:
            self.cur.execute("SELECT * FROM products WHERE product_name = %s",(self.product_name,))
            return self.cur.fetchone()
        except Exception as e:
            self.cur.close
            self.conn.close

    def get_product_by_id(self):
        """This method check wheather a product is in the system.
           :param:product_id.
        """
        print(self.product_id)
        try:
            self.cur.execute("SELECT * FROM products WHERE product_id = %s",(self.product_id,))
            return self.cur.fetchone()
        except Exception as e:
            self.cur.close
            self.conn.close



    def get_products(self):
        """This method gets all products in the system.
           :return:products:
        """
        try:
            self.cur.execute("SELECT * FROM products")
            return self.cur.fetchall()
        except Exception as e:
            self.cur.close
            self.conn.close


    def delete_product(self):
        """This method deletes a products from the database.
           :return:delete message:
        """
        if not self.get_product_by_id():
            return dict(message = "This product is not in the system")
        try:
            self.cur.execute("DELETE FROM products WHERE product_id = %s", (self.product_id,))
            self.conn.commit()
            return dict(message = "one product deleted")
        except Exception as e:
            self.cur.close
            self.conn.close

    def update_product(self):

        query = """UPDATE products set description = %s, category = %s, price = %s, stock = %s"+
        "min_stock = %s WHERE product_id = %s  """

        try:
            self.cur.execute(query, (self.description, self.category, self.price, self.stock, self.minStock,self.product_id,))
            self.conn.commit()
            return dict(message = "Updated succesfuly")
        except Exception as e:
            self.cur.close
            self.conn.close
