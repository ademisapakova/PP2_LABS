n = int(input()) 

students = dict() 
 
for i in range(n):
    s=input().split()
    name = s[0]
    mon = int(s[1])
    if name not in students:
        students[name] = mon
    else:
        students[name]+=mon

maxi = int(0)

for i in students.values():
    if int(i)>maxi:
        maxi=i

for k,v in sorted(students.items()):
    if v==maxi:
        print("{} is lucky!".format(k))
    else:
        print("{} has to receive {} tenge".format(k, maxi - v))