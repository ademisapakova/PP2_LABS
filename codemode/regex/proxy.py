import re

with open('input.txt', 'r') as f:
    x = f.readlines()


pattern = r'(?P<ip>^.+):(?P<host>\d{4})@(?P<user>.+):(?P<pass>.*)'

patric = re.compile(pattern)

for i in patric.finditer(x):
    print(i.group('ip'))