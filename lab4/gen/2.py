n = int(input())

def even(n):
    for i in range(0,n+1,2):
        if i==n and n%2==0:
            print(i)
            exit()
        elif i==n-1 and n%2!=0:
            print(i)
            exit()    
        print(i, end=",")


even(n)        