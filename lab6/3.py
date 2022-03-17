#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
a = input()
print('PALINDROME!') if a == ''.join(reversed(a)) else print('NOT PALINDROME!')