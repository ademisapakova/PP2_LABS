l1=list(map(int,input().split()))

#print(*l1)

for i in range(len(l1)):
    if sum(l1[:i])==sum(l1[i+1]):
        print(i)
        exit()

print(-1)        

