n = int(input()) 
arr = [] 
for i in range(n): 
    s = input() 
    if("@gmail.com" in s): 
        index = s.find("@gmail.com") 
        s = s[:index] 
        arr.append(s) 
        
for i in arr: 
    print(i)