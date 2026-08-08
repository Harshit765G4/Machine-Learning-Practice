from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1}: {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to be created: ")
        p = Path(name)
        if not p.exists() and p.is_file():
            with open(p, "w") as fs: # creating a new file - Write creates file or Overwrites the existing file
                        data = input("Enter the data to be written in the file: ")
                        fs.write(data)
                    
            print(f"File '{name}' created successfully.")   
        else:
            print(f"File '{name}' already exists.")
    except Exception as err:
        print(f"Error occurred while creating the file: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to be read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data =fs.read()
                print(f"Contents of the file '{name}':\n{data}")
            print(f"File '{name}' read successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error occurred while reading the file: {err}")   

def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to be updated: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Choose the update mode:")
            print("press 1 for changing the name of the file")
            print("press 2 for overwriting the data of the file")
            print("press 3 for appending some content in your file")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name2 = input("Enter the new name of the file: ")
                p2 = Path(name2)
                p.rename(p2)
                print(f"File '{name}' renamed to '{name2}' successfully.")
            elif choice == 2:
                with open(p, "w") as fs:
                    data = input("Enter the new data to be written in the file: ")
                    fs.write(data)
                print(f"File '{name}' updated successfully.")
            elif choice == 3:
                with open(p, "a") as fs:
                    data = input("Enter the data to be appended in the file: ")
                    fs.write(" " + data)
                print(f"Data appended to file '{name}' successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error occurred while updating the file: {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file to be deleted: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)  # deleting the file or you can use p.unlink() as well for deleting the file
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as err:
        print(f"Error occurred while deleting the file: {err}")

print("press 1 for Creating a file")
print("press 2 for Reading a file")
print("press 3 for Updating a file")
print("press 4 for Deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid choice. Please enter a number between 1 and 4.")