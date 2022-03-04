import re

emails = [
    'duramash.02@gmail.com84565',
    'z_ashimov@kbtu.kz',
    'vovka254it.it',
    'qwerty@sdfh'

]

pattern = r'^.+@[a-z]+\.[a-z]+$'

for i in emails:
    if re.match(pattern,i):
        print(f'Email{i} is valid!')


    else:
         print(f'Email{i} is not valid!')

        