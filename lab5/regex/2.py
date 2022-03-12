import re

pattern=r'ab{2,3}'

text = input()


for i in text:
    if(re.findall(pattern,i)):
        print(i)