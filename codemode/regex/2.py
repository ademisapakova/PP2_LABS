import re

email = 'duramash.02@gmail.com'
#pattern = r'\d+'
#pattern = r'\d*'
#pattern = r'\d?'
#pattern = r'.*'
#pattern = r'\.com\$$'
pattern = r'\.com$'

s = ''


#print(re.search(pattern,s))
print(re.search(pattern,email))