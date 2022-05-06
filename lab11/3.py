# Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
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