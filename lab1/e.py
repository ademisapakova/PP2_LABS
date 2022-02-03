x,y=map(int,input().split())
flag=True

num=int(x/2)
for i in range(2,num+1):
    if(x%i==0):
        flag=False
        break
if (x<=500 and y%2==0 and flag!=False):
    print("Good job!")

else:
    print("Try next time!")   