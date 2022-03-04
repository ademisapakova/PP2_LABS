import os 


while True:
    command = input()

    if command == 'cd':
        kuda = input()
        if os.path.isdir(kuda) and os.path.exists(kuda):
            os.chdir(kuda)
            print('Done')
        else:
            print('Not a directory')    

    elif command == 'dir':
        print(os.listdir(os.getcwd()),sep='\n')        
    elif command == 'gdeya':
        print(f'The current directory is : [{os.getcwd()}]')
    elif command == 'del':
        chto = input()
        if os.path.exists(chto):
            os.remove(chto)
            print("DONE")
        else:
            print("There is no such file")
    elif command == 'create dir':
        imya = input()
        if os.path.exists(imya):
            print("Uzhe est'")
        else:    
            os.mkdir(imya)   
    elif command == 'create file':            
        imya = input()
        if os.path.exists(imya):
            print("Uzhe est'")
        else:
            f = open(imya,'w')
            s = input("che napisat?") 
            f.write(s)
            f.close()
            print(f"created {imya}")   



    elif command == 'exit':
        break
