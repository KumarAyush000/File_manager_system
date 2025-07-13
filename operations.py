# file containing operations to be perforemed:
import os
import shutil

# create a foler:
def create_folder():
    folder = input("Enter folder name: ").strip()
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Folder : ({folder}) created successfully.")
    else:
        print(f"Folder : ({folder}) already exists")

# create a file:
def create_file():
    file = input("Enter file name: ").strip()
    if not os.path.exists(file):
        with open(file, "w") as f:
            write = input("Write something inside the file: ")
            f.write(write)
    else:
        print(f"File : ({file}) already exists.")

# list all items
def list_files_folders():
    path = input("Enter folder path to list (leave empty for current directory): ").strip()
    path = path if path else "."

    if os.path.exists(path):
        items = os.listdir(path)
        if items:
            print("\n📁 Contents:")
            for i in items:
                print(f"→ '{i}'")
        else:
            print(" Folder is empty.")
    else:
        print(" Path does not exist.")



# rename files/folders:
def rename_item():
    old_name = input("Enter file/folder path to rename: ").strip()
    if os.path.exists(old_name):
        new_name = input("Enter new name: ").strip()
        os.rename(old_name, new_name)
        print(f"{old_name} : changed to -->  {new_name} : new name")
    else:
        print("File/Folder does not exists")


# remove a file:
def delete_item():
    name = input("Enter file/folder name to delete: ").strip()
    if os.path.isfile(name):
        os.remove(name)
        print(f"File '{name}' deleted.")
    elif os.path.isdir(name):
        shutil.rmtree(name)  # will remove the whole folder including all the sub folders and file
        print(f"Folder '{name}' deleted.")
    else:
        print("Item not found.")

            
                
# move a file:
def move_file():
    src = input("Enter source file name: ").strip()
    if os.path.exists(src) and os.path.isfile(src):
        dest = input("Enter destination folder name: ").strip()
        if os.path.exists(dest) and os.path.isdir(dest):
            
            shutil.move(src, dest) # will move source file to destination folder
            print("File moved successfully.")
        else:
            print(f"Destination folder does not exists or is not a folder.")
    else:
        print(f"Source file: {src} does not exists.")
        

    