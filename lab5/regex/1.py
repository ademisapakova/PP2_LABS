import re

text = input()

pattern = r'ab*'

x = re.search(pattern,text) 
print('Yes' if x else "No")