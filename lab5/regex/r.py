import re

with open ('raw.data', 'r', encoding = 'utf-8') as f:
    x = f.read()

pattern = r'((?P<s>БИН)\s(?P<bin>\d+))'

print(re.search(pattern,x).group('s','bin'))

