z = int(input()) 
c = input() 
 
if c == 'k': 
    k = str(input()) 
    num = "{:." + k + "f}" 
    print(num.format(z/1024)) 
else: 
    print(z*1024)