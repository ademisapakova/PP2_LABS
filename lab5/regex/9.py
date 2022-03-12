import re

a, t = input(), ''

pattern = r'[A-Z][a-z]*'
k = re.findall(pattern, a)
for i in range (len(k)):
    t += k[i]
    if i != len(k) - 1:
        t+=' '
print(t)