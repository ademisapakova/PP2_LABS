import math
a,b = map(int,input().split())
c = int(input())
one = []
two = []
three = []
four = []
dict = {}
for i in range(c): 
  d,f = map(int,input().split())
  one.append(d)
  two.append(f)
  dict[math.sqrt(((d-a)*(d-a))+((f-b)*(f-b)))]=i
  three.append(math.sqrt(((d-a)*(d-a))+((f-b)*(f-b))))

three.sort()
for i in range(c):
   for x in dict:
     if(three[i] == x):
         four.append(dict[x])
         
for i in four:
    print(one[int(i)],two[int(i)])