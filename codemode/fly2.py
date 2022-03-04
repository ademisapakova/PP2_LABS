n=int(input())
cities=set()
mydict={}

for _ in range(n):
    a,b=input().split()
    mydict[a]=b
    cities.add(a)
    cities.add(b)

for city in cities:
    if city not in mydict.keys():
        print(city)    
        break