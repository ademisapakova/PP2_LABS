l1=list(map(int,input().split()))
arr = [l1[::-1]]
while True:

    l1=list(map(int,input().split()))
    l2=l1[::-1]
    if len(l1)==1:
        break
    else:
        arr.append(l2)

arr.sort()   
for i in arr:
    y=str(i[0])
    m=str(i[1])
    d=str(i[2])

    while len(y)!=4:
        y='0'+y
    i[0]=y    
    while len(m)!=2:
        m='0'+m
    i[1]=m
    while len(d)!=2:
        d='0'+d
    i[2]=d    

for i in arr:
    i.reverse()
    print(*i)
