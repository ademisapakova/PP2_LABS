import re
text=[
    "dfdfghjkrtyuivbnaJDCLJLKJb",
    "dsf",
    "gsajhagjkhkjhjhhaba",
    "aghjb",
    "lkjkl/////ob",
    "WRRRRroob"
]
pattern=r'a.+b$'
for i in text:
    if(re.findall(pattern,i)):
        print(i)