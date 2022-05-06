# Create procedure to insert new user by name and phone, update phone if user already exists

from genericpath import exists
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='tmrivion'
)

current = config.cursor()

id = input("Enter ID: ")
username = input("Username:")
phone = input("Phone: ")
email = input("Email: ")

if id EXISTS:
    
    sql = '''
            UPDATE phonebook SET username = %s, phone = %s, email = %s WHERE id = %s;
        '''
    current.execute(sql, (username, phone, email))

else:

    sql1= '''
    UPDATE phonebook SET username = %s, phone = %s, email = %s, id = %s;
    '''

current.execute(sql)

final = current.fetchall()
print(final)

current.close()
config.commit()
config.close()