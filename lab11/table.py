#Design tables for PhoneBook.
import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='tmrivion'
)

current = config.cursor()

current.execute(
    '''
    CREATE TABLE phonebook3(
        name VARCHAR(20),
        phonenumber VARCHAR(12)
    )
    '''
)

config.commit()
current.close()
config.close()