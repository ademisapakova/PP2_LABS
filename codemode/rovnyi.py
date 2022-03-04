# Alikhan isStraight
a, pos, pali = list(map(int, input().split())), 0, 0
for i in range(len(a)):
    if a[i] > 0:
        pos += 1
    t = str(a[i])
    if str(a[i]) == t[::-1]:
        pali += 1
if pos == len(a) and pali == len(a):
    print('Rovnyi')
else:
    print('Ne rovnyi')
# 12 22 33 44 55
# Ne rovnyi