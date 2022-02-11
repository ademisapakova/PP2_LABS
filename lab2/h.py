main_x, main_y = map(int ,input().split()) 
n = int(input()) 
res = dict() 
 

for i in range(n): 
    x, y = map(int, input().split()) 
    s = pow(pow((x - main_x), 2) + pow((y - main_y), 2), 1/2) 
    if s not in res: 
        res[s] = [x, y] 
    else: 
        res[s].append(x) 
        res[s].append(y) 
 
for k in sorted(res.keys()): 
    v = res[k] 
    if len(v) > 2: 
        for i in range(0, len(v), 2): 
            print(v[i], v[i+1]) 
 
    else:         
        print(*res[k])