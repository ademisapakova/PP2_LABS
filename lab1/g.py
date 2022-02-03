def todecimal(x):
    if x == 0:
        return 0
    else:
        return(x%10 + 2*todecimal(x//10))

x=int(input())
print(todecimal(x))