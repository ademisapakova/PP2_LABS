import os

mypath = input()

print('Existing:', os.path.exists(mypath))

if os.path.exists(mypath):
    print('Filename:', os.path.basename(mypath))
    print('Dirname:', os.path.dirname(mypath))
# Input:
#  C:\Users\Дом\Desktop\labs\PP2_LABS\lab6\dir\2.py

# Output:
# Existing: True
# Filename: 3.py
# Dirname:  C:\Users\Дом\Desktop\labs\PP2_LABS\lab6\dir