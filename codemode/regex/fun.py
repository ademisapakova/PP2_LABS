import re

with open('t.txt', 'r', encoding = 'utf-8') as f:
    x = f.read()

pattern = r'def\s(?P<fun>\w+)'

arr = re.findall(pattern, x)

print(*arr,sep = '\n')


