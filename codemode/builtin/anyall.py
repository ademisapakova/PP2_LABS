#all, any()

my_list = [ 2, 5, 7, 566, 12, 43]

def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True 



for i in my_list:
    if prime(i):
        print(i)  


if all([prime(i) for i in my_list]):
    print('All numbers are prime')

else:
    print("Not all")    