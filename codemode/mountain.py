from multiprocessing.spawn import is_forking


arr=list(map(int,input().split()))

if len(arr)<3:
    if len(arr)!=3:
        print('No')
        exit()


   