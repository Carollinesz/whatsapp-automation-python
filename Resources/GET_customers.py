from .db_connect import connection

cursor = connection()[0]

cursor.execute('SELECT name, phone FROM customers')
customer_list = cursor.fetchall()