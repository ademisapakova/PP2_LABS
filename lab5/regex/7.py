import re

a, t = input(), ''
a = a.split('_')
print(a)
for i in a:
    t += i.capitalize()
print(t)
