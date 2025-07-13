
# 🗂️ Python File Management System (with Admin Login)

This is a command-line based **File Management System** built in Python. It allows an admin user to perform file and folder operations such as creating, renaming, deleting, listing, and moving files/folders using built-in Python modules like `os` and `shutil`.

---

## 🚀 Features

- 🔐 **Admin Login System** with retry attempts  
- 📝 **Create** folders and files with custom input  
- 📁 **List** all contents of a directory  
- ✏️ **Rename** files or folders  
- ❌ **Delete** files or folders  
- 🚚 **Move** files from one location to another  
- ✅ Input validation and robust error handling  
- 📦 Modular design: logic is divided across multiple files for better organization

---

## 🛠️ Technologies Used

- **Python 3.10+**
- `os` module
- `shutil` module

---

## 📂 Project Structure

```

file-manager/
│
├── main.py               # Entry point
├── login.py              # Admin login system
├── filemanager.py        # Main menu and controller
├── operations.py         # File and folder operations
├── test.txt              # Sample file for testing
├── README.md             # Project documentation
└── data/                 # (optional) destination folder for moving files

````

---

## 🧪 How to Run

1. Make sure you have **Python 3.10+** installed.
2. Clone/download this repository.
3. Open a terminal in the project folder.
4. Run the program using:
```bash
python main.py
````

---

## 🔑 Admin Login

The system contains predefined usernames and passwords stored in the `login.py` file. You can update or expand them as needed.

---

## 📸 Sample Usage

```
Welcome to the File Management System

1. Create Folder
2. Create File
3. List Files and Folders
4. Rename File/Folder
5. Delete File/Folder
6. Move File
7. Exit
```

---

## 💡 Future Enhancements

* Password encryption using `hashlib`
* Store user activity logs
* Add file content preview
* Create a GUI using Tkinter or PyQt

---

## 👨‍💻 Author

Developed By - @KumarAyush000

---

## 📜 License

This project is open-source and free to use for educational purposes.

