import re

dates = [
    '32.01.2022',
    '29.02.2019',
    '15.05.2003',
    '22.14.1901',
    '22/11/1901'
]

#format dd.mm.yyyy
#01.01.1900 - 31.12.2022 

#pattern = '([0-2][0-9])|3[01])'

# 01-09 10 11 12 ... 20 ... 30 31
pattern = r'(?P<day>0[1-9]|[1-2][0-9]|3[01])[./](?P<month>0[1-9]|1[0-2])(\.|/)(?P<year>19\d{2}|20[0-1]\d|202[0-2])'

for i in dates:
    if re.match(pattern, i):
    
        day = re.match(pattern,i).group('day')
        month = re.match(pattern,i).group('month')
        year = re.match(pattern,i).group('year')
        print(day,month,year)
    else:
        print('Not valid year!')