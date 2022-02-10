x=input()
arr=[]

for i in x:
    if i=='(' or i=='{' or i=='[':
        arr.append(i)
    else:
        if len(arr)==0:
            print('No')
            exit()
              
        top=arr[len(arr)-1]
        if i==')' and top!='(' or i=='}' and top!='{' or i==']' and top!='[':
         print('No')
         exit()
        arr.pop()    
     
if len(arr)!=0:
    print('No') 
else:
    print('Yes')       
