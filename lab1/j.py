m = input() 
s = m.split(" ") 
t = "" 

for i in s: 
    if(len(i) >= 3): 
        t += i + " " 
 
 
print(t)
