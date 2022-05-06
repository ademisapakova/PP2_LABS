# Create function to querying data from the tables with pagination (by limit and offset)

import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='tmrivion'
)

current = config.cursor()

sql = '''


'''
        
current.execute(sql)

final = current.fetchall()
print(final)
current.close()
config.commit()
config.close()