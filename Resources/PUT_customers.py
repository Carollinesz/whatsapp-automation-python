from .validation import validation
from .db_connect import connection
import csv

class db_commands:
    cursor, conn = connection()
    
    @staticmethod
    def add(name, phone):
        phone = validation.validation(phone)
        try:
            db_commands.cursor.execute(f'INSERT INTO customers (name, phone) VALUES ("{name}", "{phone}")')
            db_commands.conn.commit()
            print('Sucessful!!!')
        except:
            print('This number already exist in database, please remove it or try other')
            exit()


    def add_list():
            with open(r'Assets\phone_list.csv','r',newline='',) as phone_list:
                reader = csv.reader(phone_list)
                for row in reader:
                    name = row[0].strip()
                    phone = row[1].strip()
                    phone = validation.validation(phone)
                    try:
                        db_commands.cursor.execute(f'INSERT INTO customers (name, phone) VALUES ("{name}", "{phone}")')
                        db_commands.conn.commit()
                    except:
                        print('This number already exist in database, please remove it or try other')
                        exit()
                print('Successful!!!')

    def remove_phone(phone):
        phone = validation.validation(phone)
        db_commands.cursor.execute(f'DELETE FROM customers WHERE phone = "{phone}"')
        db_commands.conn.commit()
        print('Successful!!!')

    def remove_all_phones():
        db_commands.cursor.execute(f'DELETE FROM customers')
        db_commands.conn.commit()