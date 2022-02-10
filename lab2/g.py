n = int(input())
demons = dict()

for i in range(n):
    s=input().split()
    weap=s[1]
    if s[1] not in demons:
        demons[weap]=1
    else:
        demons[weap]+=1    
m = int(input())

hunters = dict()

for i in range(m):
    h = input().split()
    weap=h[1]
    if weap not in hunters:
        hunters[weap]=int(h[2])
    else:
        hunters[weap]+=int(h[2])

time = 0

for i in demons.keys():
    for j in hunters.keys():
        if i==j:
            if demons[i]<hunters[j]:
                time+=demons[i]
            else:
                time+=hunters[j]

 
ans = n - time

print("Demons left: {}".format(ans))



 