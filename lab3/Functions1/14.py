def reversed(s):
    c = []
    for i in range(len(s)-1, -1, -1):
        c.append(s[i])
    return c
print(*reversed(input().split()))


def spygame(a):
    s = ''
    for i in a:
        if i == 0 or i == 7: 
            s += str(i)
    if '007' in s:
        return True
    else: return False
print(spygame(list(map(int, input().split()))))


def palindrome (s):
    s1 = s[::-1]
    if s1 == s: print('Palindrome!')
    else: print('Not palindrome!')
palindrome(input())