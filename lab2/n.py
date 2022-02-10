arr=[]
res=[]
a=1
while a!=0:
    a=int(input())
    if(int(a!=0)):
        arr.append(a)


l=len(arr)
for i in range(int(l/2)):
    res.append(arr[i]+arr[len(arr)-i-1])
if len(arr)%2!=0:
    res.append(arr[int(l/2)])
print(*res)   
