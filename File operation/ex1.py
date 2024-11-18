import os

# file1.txt will be created in this python code folder
File = open("file1.txt", "w")
File.write("Python has functions for ")
File.close()

File = open("file1.txt", "r")
print(File.read())
File.close()

File = open("file1.txt", "a")
File.write("creating, reading, writing and deleting files.")
File.close()

File = open("file1.txt", "r")
print(File.read())
File.close()

# remove # after file1.txt is created in your python code folder
#os.remove("file1.txt")