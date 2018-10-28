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

        self.cur.execute("INSERT INTO products(product_id,product_name,description,category,price,stock,min_stock)"+
        "VALUES(%s,%s,%s,%s,%s,%s,%s)", (product_id,product_name,description,category,price,stock,minStock,))
        self.conn.commit()

        return dict(message = product_name+" succesfuly added")
