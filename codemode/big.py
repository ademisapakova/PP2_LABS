def fac(x):
    ans=1
    for i in range(1,x+1):
        ans*=i
    return ans    

arr=list(map(int,input().split()))
n=int(input())
cnt=0
f=fac(n)

    

for i in range(len(arr)):
    if arr[i]>f:
        cnt+=1


if(cnt==0):
    print(0)
else:
    print(cnt)    

'''
    # Print the amount of big numbers; the number is big, if it's bigger that the factorial of n
def fac(x):
    res = 1
    for i in range(1, x + 1):
        res *= i
    return res
a, b = list(map(int, input().split())), int(input())
r = fac(b)
res = 0
for i in range(len(a)):
    if a[i] > r:
        res += 1
print(res)
'''