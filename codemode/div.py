'''
5 9 13 52
3

8 27 56 901
'''

l1=list(map(int,input().split()))
div = int(input())
for i in range(len(l1)):
    print(((l1[i]*l1[i]))//div,end=" ")