import os
import psycopg2
from flask import Flask
from werkzeug.security import generate_password_hash
from instance.config import app_config
enviroment = os.environ['ENVIRONMENT']
class DbBase(object):
	"""This Class has the setup for connecting to the database and creation of tables """


	def connection(self):
		"""This method creates a connection to the class
		   param:con
		   return:connection

		"""
		conn = psycopg2.connect(app_config[enviroment].connectionVariables)
		return conn

	def createTables(self):
		"""This method creates all tables if they dont exist
           param1:connection
           param2:queries
           param3:cursor
		"""

		conn = self.connection()
		cur=conn.cursor()

		query1 = """CREATE TABLE if not EXISTS users(
		user_id Serial  PRIMARY KEY NOT NULL,
		names varchar(40) NOT NULL,
		email varchar(100)  NOT NULL,
		password varchar(500) NOT NULL,
		role varchar(15) NOT NULL)
		"""

		query2 = """CREATE TABLE if not EXISTS products(
		product_id serial  NOT NULL,
		product_name varchar(200)  NOT NULL,
		description varchar(200),
		category varchar(20),
		price integer NOT NULL,
		min_stock integer NOT NULL,
		stock integer NOT NULL)
		"""


		query3 = """CREATE TABLE if not EXISTS sales(
		product_name varchar(200) NOT NULL,
		quantity INTEGER NOT NULL,
		subtotal INTEGER NOT NULL,
		sale_id INTEGER NOT NULL)
		"""


		query4 = """CREATE TABLE if not EXISTS transactions(
		sale_id serial NOT NULL,
		total INTEGER NOT NULL,
		product_count integer NOT NULL,
		user_id varchar(20) NOT NULL)
		"""



		query5 = """CREATE TABLE if not EXISTS blacklist(
		token_id serial NOT NULL,
		json_token varchar(700) NOT NULL
		)
		"""

		queries=[query1, query2,  query3, query4, query5]

		for query in queries:

			cur.execute(query)

		conn.commit()
		conn.close()



	def create_store_owner(self):
		"""This method creates the default users
           :param1:names.
		   :param2:email.
		   :param3:role.
		   :param4:password.
		"""
		conn = self.connection()
		cur=conn.cursor()
		if not self.select_one_user("admin@quickwear.com"):

		    password = generate_password_hash('@Admin1')
		    cur.execute("INSERT INTO users(email,names,password,role) VALUES(%s,%s,%s,%s)",
		    ('admin@quickwear.com', 'Sammy Njau',password,'admin'))
		    conn.commit()
		    conn.close()

	def select_one_user(self,email):
		"""This method gets one user from the system
           param1:email
		"""
		conn = self.connection()
		cur=conn.cursor()
		cur.execute("SELECT * FROM users where email =%s",(email,))
		return cur.fetchone()

	def dropTables(self):


		 query1="""DROP TABLE if EXISTS users CASCADE"""
		 query2="""DROP TABLE if EXISTS products CASCADE"""
		 query3="""DROP TABLE if EXISTS sales CASCADE"""
		 queries = [query1,query2,query3]

		 conn = self.connection()
		 cur=conn.cursor()

		 for query in queries:

			 cur.execute(query)
		 conn.commit()
		 cur.close()
		 conn.close
