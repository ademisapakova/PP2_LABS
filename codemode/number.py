n = int(input())
cap = 0
vow = 0
dig = 0


for i in range(n):
    a, b, c = input().split()

    for i in range(len(a)):
         if a[i] >= 'A' and a[i] <= 'Z':
            cap += 1
    for i in range(len(b)):
        if b[i] == 'a' or b[i] == 'o' or b[i] == 'e' or b[i] == 'u' or b[i] == 'i':
            vow += 1
    for i in range(len(c)):
        if c[i].isdigit:
            dig += 1

print(cap, vow, dig)
