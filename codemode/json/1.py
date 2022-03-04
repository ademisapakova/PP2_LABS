import json

f = open('task.json', 'r')
temp = f.read()

dd = json.loads(temp)

dd['myName'] = 'ourName'
dd['nums'].sort()
dd['heroes']['spider-man'] = 'Tom'


for k,v in dd.items():
    print('{} : {}'.format(k,v))

for k,v in dd.items():
    print('{} : {}'.format(k,v))

y = json.dumps(dd, indent = 4)
with open('res.json', 'w') as f:
    f.write(y)

