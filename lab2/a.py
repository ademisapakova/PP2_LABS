a,b = list(map(int, input().split())),0
for i in a:  
    for j in range(b, b + 1 + a[b]): 
        if b + 1 + a[b] >= len(a): 
            print(1)
            exit(0)
        if b + a[b] < a[j] + j:   
            b = j
print(0)