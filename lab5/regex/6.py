import re

text=[
    "vbn poiuyt drfgbnhj",
    "bnm,ppn.qwertya",
    "ghh fds ds"
]
pattern=r'\s|\.|\,'
for i in text:
    x=re.sub(pattern,':',i)
    print(x)