n=int(input())
put=[]
take=[]

for i in range(n):
    x=input().split()
    if len(x)==2:
        num=int(x[0])
        disk=x[1]
        put.append(disk)
    else:
        take.append(put[0])
        put.pop(0)
print(*take)        
