from operations import *

def file_manager():
    while True:
        print("\n","---"*3 ,"WELCOME TO FILE MANAGER","---"*3, "\n" )
        print(f"(1) - Create Folder")
        print(f"(2) - Create File")
        print(f"(3) - List all items")
        print(f"(4) - Rename items")
        print(f"(5) - Delete items")
        print(f"(6) - Move items")
        print(f"(q) - Exit the system")
        
        choice = input("\nEnter your choice: ")
        if choice == "1":
            create_folder()
            continue
        elif choice == "2":
            create_file()
            continue
        elif choice == "3":
            list_files_folders()
            continue
        elif choice == "4":
            rename_item()
            continue
        elif choice == "5":
            delete_item()
            continue
        elif choice == "6":
            move_file()
            continue
        elif choice.lower() == "q":
            print("Exiting file manager...\n")
            break
        
        