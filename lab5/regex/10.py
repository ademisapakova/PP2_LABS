import re
pattern=r'[A-Z][a-z]*'
a=re.findall(pattern,"FghjklAikokdslajA")
t=""
for i in range(len(a)):
   t+=a[i]
   if i!=(len(a)-1):
       t+='_'
print(t)