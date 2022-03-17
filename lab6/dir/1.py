#Write a Python program to list only directories, files and all directories, files in a specified path.
import os
path = r'C:\Users\Дом\Desktop\labs'
print("Our directories:", [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))])
print("Our files:")
print([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))])
print("All directories and files:")
print([i for i in os.listdir(path)])


