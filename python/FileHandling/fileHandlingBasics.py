# File handling basics in python
# file handling is an important part of any web application. Python has several functions for creating, reading, updating, and deleting files.
#it follows CRUD Operations (Create, Read, Update, Delete)

# Opening a file in read mode

p = open(r'C:\Users\Hey_Nerd\Machine Learning\python\ExceptionHandling\ExceptionHandlingBasics.py')

print(p.read())  # reading the file



new_file = open("Sample.txt", "w")  # creating a new file - Write creates file or Overwrites the existing file

new_file.write("This is a sample text file.\n")  # writing to the file
new_file.write("This is the second line of the file.\n")

new_file.close()  # closing the file

new_file = open("Sample.txt", "a")  # opening the file in append mode
new_file.write("This is the third line of the file added using append mode.\n")  # appending
new_file.close()  # closing the file


new_file = open("Sample.txt", "r")  # Reading a File
print(new_file.read())  # reading the file


new_file = open("SampleUsingX.txt", "x")  # Creating a new file in exclusive creation mode
new_file.write("This is a sample text file created using 'x' mode.\n")
new_file.close()  # closing the file