import re

with open ('raw.data', 'r', encoding = 'utf-8') as f:
    x = f.read()


pattern = r'БИН\s(?P<bin>\d+)'
pattern2 = 'Серия\s(?P<series>\d+)'
#   БИН 080841000761

print(re.search(pattern,x).group('bin'))
print(re.search(pattern2,x).group('series'))