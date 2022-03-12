import re
text=[
    "AAsDa",
    "adfAfghjk",
    "dsasdfghjkalA",
    "KJDSLKJDL:JL:Ja",
    "JSKHAahjgk",
    'KSDJASdklsdA'
    ]
pattern=r'[A-Z]{1}[a-z]+$'
for i in text:
  if re.findall(pattern,i):
    a=re.findall(pattern,i)
    print(a)