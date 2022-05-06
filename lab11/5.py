# Implement procedure to deleting data from tables by username or phone

import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='tmrivion'
)

current = config.cursor()

sql = '''
      SELECT FROM phonebook WHERE username = 'adema';
'''
        
current.execute(sql)

current.close()
config.commit()
config.close()