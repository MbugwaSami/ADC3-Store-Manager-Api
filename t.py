import psycopg2

def createtable():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='Mwoboko10@' host='localhost' port='5432'")
    cur=conn.cursor()
    q="""
    CREATE TABLE if not exists store(item text,quantity integer,price real)"""
    cur.execute(q)
    conn.commit()
    conn.close()
createtable()       