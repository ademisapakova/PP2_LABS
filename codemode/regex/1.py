import re

s = 'abcabpdabc'
pattern = r'ab'
print(re.search(pattern, s))
print(re.findall(pattern, s))


for i in re.finditer(pattern,s):
    print (i)
    print(i.span())
    print(i.start())

t = 'StudentsA12workersA45employees'
print(re.split(r'A\d+', t))
print(re.sub(r'A', 'AUE', t))
print(re.sub(r'\d+', '!!', t))

