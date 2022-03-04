n=int(input())
fir,sec = set(), set()
for i in range(n):
    a,b = input().split()
    fir.add(a)
    sec.add(b)

print(*sec.difference(fir))
