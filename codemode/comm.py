arr=list(map(str,input().split()))
set1=set(arr[0])
for i in range(1, len(arr)):
   set1= set1.intersection(set(arr[i]))
print(*sorted(set1), sep="")
