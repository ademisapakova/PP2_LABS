import os

print(os.getlogin())
print(os.getcwd())
print(os.getcwd())

#os.mkdir('test_folder')

print(os.listdir(path=".")) #what folders are there at CW

os.сhdir(r"C:\Users\Дом\Desktop\labs\PP2_LABS\codemode\os\test_folder")

for i in range(10):
    f = open(str(i+1)+'txt','w')