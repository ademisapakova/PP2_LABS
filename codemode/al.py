'''
arr=list(map(str,input().split()))

for i in arr:
     alphabet_position(i)
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
'''
    # Alphabet
s=input().lower()
for i in range(len(s)):
    if 96 < ord(s[i]) < 123:
        print((ord(s[i])-96),end=' ')
