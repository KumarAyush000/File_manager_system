from filemanager import *


# admin data
admin_data = {
    "Admin1" :"pass123",
    "Admin2" :"0000000",
    "Admin3" :"abd123",
    "Admin4" :"pass456"
}

# admin log in function

def admin_login():
    while True:
        print("\n","---"*3,"Welocome to the log in page", "---"*3 ,"\n")
        name = input("Enter username ('q' to EXIT): ").strip()
        if name.lower() == "q":
            print("Exiting the login system...\n")
            break
        elif name in admin_data:
            tries = 3
            while tries != 0:
                password = input("Enter password: ")
                if password == admin_data[name]:
                    file_manager()
                    return 
                else:
                    tries -= 1
                    if tries == 0:
                        print(f"No tries left. Exiting")
                        break
                    else:
                        print(f"Incorrect password. Tries left : {tries}")
                        continue
        else:
            print("Invalid username.")
            continue
        

            
            
            