import os


os.chdir(r"C:\Users\Дом\Desktop\labs\PP2_LABS\codemode\os\test_folder")

for i in range(10):
    f = open(str(i+1)+'txt','w')

f.close()    


for i in range(5):
    os.mkdir(f'{i+1}')
    os.chdir(os.path.join(os.getcwd(),f'{i+1}'))