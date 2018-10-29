from ..models import Models

class Products(Models):
    """
    This class has methods for manipulation of products data.
    """


    def add_product(self,product_id,product_name,description,category,price,stock,minStock):
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
            self.cur.execute("INSERT INTO products(product_id,product_name,description,category,price,stock,min_stock)"+
            "VALUES(%s,%s,%s,%s,%s,%s,%s)", (product_id,product_name,description,category,price,stock,minStock,))
            self.conn.commit()
        except Exception as e:
            self.cur.close
            self.conn.close

        return dict(message = product_name+" succesfuly added")

    def get_one_product(self,param):
        """This method check wheather a product is in the system.
           :param:product_id/product_name.
        """
        try:
            self.cur.execute("SELECT * FROM products WHERE product_name = %s OR product_id= %s",(param,param,))
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


    def delete_product(self,product_id):
        """This method deletes a products from the database.
           :return:delete message:
        """
        if not self.get_one_product(product_id):
            return dict(message = "This product is not in the system")
        try:
            self.cur.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            self.cur.commit()
            return dict(message = "one product deleted")
        except Exception as e:
            self.cur.close
            self.conn.close

    def update_product(self,description, category, price, stock, minStock):

        query = """UPDATE products set description = %s, category = %s, price = %s, stock = %s"+
        "min_stock = %s WHERE product_id = %s  """

        try:
            self.cur.execute(query, (description, category, price, stock, minStock,))
            self.cur.commit()
            return dict(message = "Updated succesfuly")
        except Exception as e:
            self.cur.close
            self.conn.close
