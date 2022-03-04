import re

passwords = [
  "SDF#$%56bn",
  "987!@YHBv",
  "adilIjaks",
  "Group_1",
  "group-adin",
  "GRUPPA-DYVA"
]


pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_!@#$]).{6,12}'

for i in passwords:
    if re.search(pattern, i):
        print('Valid')
    else:
        print('Nope')    
