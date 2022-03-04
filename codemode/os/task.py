import os

cnt = 0
while True:
    cmd = input()
    if cmd == 'dir':
        if os.path.isdir(os.getcwd()):
            cnt+=1
            print("Number of files:", cnt)     

    elif cmd == 'owd':
        os.chdir('C:\\')

    elif cmd == 'gdeya':
        print(f'The current directory is : [{os.getcwd()}]')    
    elif cmd == 'name ch':
        s = os.getcwd()
        name = input("Old name:\n")

        old_path = s + f"\{name}"
        new_name = input("New name:\n")

        if os.path.isfile(name):
            os.rename(name,input())
            print(name)
        else:
            print("No such file")    

       


