my_list = [ 2, 5, 7, 566, 12, 43]

def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False    
    return True 

print(*filter(prime, my_list))
print(*filter(lambda x: x>=10, my_list))
#print(f'jgkogo{'}')