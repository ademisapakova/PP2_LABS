import json

f = open('task2.json', 'r')
temp = f.read()

dict = json.loads(temp)

dict['model'] = 'mac'
dict['owners'].append('hi')
dict['owners'].sort(reverse = True)
dict['why'] = 'k'
del dict['why']
dict['new'] = dict.pop('model')

for k,v in dict.items():
    print('{}: {}'.format(k,v))


y = json.dumps(dict, indent = 5)

with open('t2.json', 'w') as f:
    f.write(y)

