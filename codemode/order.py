s=input().split()
arr=[0 for i in range(10)]
for word in s:
    for i in word:
        if i.isdigit():
            arr[int(i)] = word
            break

res=' '.join([i for i in arr if i!=0])

print(res)

'''
res = " "
for i in arr:
    if i!=0:
        res+=str(i)+ ' '
print(res)  
'''       