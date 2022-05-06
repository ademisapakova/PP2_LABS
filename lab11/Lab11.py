import psycopg2
from config import database

config = psycopg2.connect(**database)
current = config.cursor()

def checkNum(number):
    if(number.find('8707') == 0 and len(number) == 11):
        return number
    elif(number.find('8747') == 0 and len(number) == 11):
        return number
    elif(number.find('8775') == 0 and len(number) == 11):
        return number
    elif(number.find('8708') == 0 and len(number) == 11):
        return number
    elif(number.find('8777') == 0 and len(number) == 11):
        return number
    elif(number.find('8778') == 0 and len(number) == 11):
        return number
    print("Sorry, it seems you made a mistake in your phone number, can you write it again?")
    number = str(input())
    return checkNum(number)

def check(name):
    select = '''
            SELECT phonenumber FROM phonebook2 WHERE name = %s;
    '''
    current.execute(select, [name])
    DICT = current.fetchone()
    if DICT == None: return True
    else: return False


print("What's your query?")
query = str(input())

if(query == 'insert'):
    #upgrade:
    # u='''
    #     create or replace procedure update(username varchar, pphonenumber varchar)
    #     as
    #     $$
    #         begin
    #             UPDATE phonebook2 
    #             SET phonenumber = $2 
    #             WHERE name = $1;
    #         end;
    #     $$ language plpgsql;
    #     call update(%s, %s);
        
    #   '''
    #insert:
    # i='''
    #     create or replace procedure insert(name varchar, phonenumber varchar)
    #     as
    #     $$
    #         begin
    #             insert into phonebook2(name, phonenumber) values ($1, $2);
    #         end; 
    #     $$ language plpgsql;  
    #     call insert(%s,%s);

    # '''

    print("How many people you want to add?")
    n = int(input())
    for _ in range(0,n):
        name = str(input())
        number = str(input())
        number = checkNum(number)
        if(check(name)): 
            current.execute("call insert(%s, %s);", (name,number))
        else:
            current.execute("call update(%s, %s);",(name,number))
        

if(query == 'delete'):
    #delete:
    # d='''
    #     create or replace procedure delete(data varchar)
    #     as
    #     $$
    #         begin
    #             delete from phonebook2 where name = $1  or phonenumber = $1; 
    #         end;
    #     $$ language plpgsql;
    #     call delete(%s);
    # '''

    data = str(input())
    current.execute("call delete(%s)", [data])
       

if(query == 'pagination'):
    print("type your limit and offset")
    limit = int(input())
    offset = int(input())
    pa = '''
        select * from phonebook2 offset %s limit %s;
    '''
    current.execute(pa ,(limit,offset))
    print(current.fetchall())


if(query == 'query'):
    #querying:
    # q='''
    #     create or replace function querying(data varchar)
    #         returns table (
    #             namee varchar,
    #             phonenumberr varchar
    #         )
    #     as
    #     $$
    #         begin
    #             return query
    #                 select * from phonebook2 where name ilike $1 or phonenumber ilike $1;
    #         end;
    #     $$ language plpgsql;
    #     select querying(%s);
    # '''

    pat = str(input())
    current.execute("select querying(%s)",["%"+pat+"%"])
    print(current.fetchall())

current.close()
config.commit()
config.close()