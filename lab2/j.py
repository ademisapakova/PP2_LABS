n = int(input()) 
pw = [] 
 
def upp(s): 
    for i in range(len(s)): 
        if s[i].isupper():  
            return True 
    return False         
 
def low(s): 
    for i in range(len(s)): 
        if s[i].islower(): 
            return True 
    return False 
 
def dig(s): 
    for i in range(len(s)): 
        if s[i].isdigit(): 
            return True             
    return False 
 
for i in range(n): 
    s = input() 
    if upp(s) and low(s) and dig(s): 
        pw.append(s) 
 
pw = set(pw) 
 
print(len(pw)) 
for i in sorted(pw): 
    print(i)