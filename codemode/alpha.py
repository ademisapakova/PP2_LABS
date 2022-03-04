'''
arr=list(map(str,input().split()))

for i in range(len(arr)):
    a=str(ord(arr[i])-96)
    print(a)
'''
   
# Alphabet
s=input().upper()
for i in range(len(s)):
    if 64 < ord(s[i]) < 91:
        print((ord(s[i])-64),end=' ')


        
# The sunset sets at twelve o' clock.
# 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11