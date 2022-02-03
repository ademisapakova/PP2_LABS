s = input() 
t = input() 
x = -1
y = -1 
for i in range(len(s)): 
    if (s[i] == t): 
        x = i 
        break 
i = len(s)-1 

while i != 0: 
    if(s[i] == t and i != x): 
        y = i 
        break 
    i -= 1 
 
if(x != -1 and y != -1): 
    print(x, y) 
elif(x != -1 and y == -1): 
    print(x)