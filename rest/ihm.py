import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.messagebox import showinfo

iduser = None
passwd = None

def on_login():
    global iduser, passwd, username_var, password_var, root
    iduser = username_var.get()
    passwd = password_var.get()
    root.destroy()  # Destroy the login window

def createLoginWindow():
    global username_var, password_var, root
    # Create main window
    root = tk.Tk()
    root.title("Login Page")

    # Username Label and Entry
    username_label = tk.Label(root, text="Username:")
    username_label.grid(row=0, column=0, padx=10, pady=5)
    username_var = tk.StringVar()
    username_entry = tk.Entry(root, textvariable=username_var)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    # Password Label and Entry
    password_label = tk.Label(root, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_var = tk.StringVar()
    password_entry = tk.Entry(root, show="*", textvariable=password_var)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Login Button
    login_button = tk.Button(root, text="Login", command=on_login)
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

def createErrorDialog(message):
    messagebox.showerror("Error", message)

def select_file():
    try:
        filetypes = (
            ('Text files', '*.txt'),
            ('All files', '*.*')
        )
    
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='./demands',
            filetypes=filetypes)
    
        return filename
    except Exception as e:
        print("Error :", e)

def return_selected_file():
    try:
        filePath = select_file()
        if filePath:
            showinfo(
                title='Selected File',
                message=filePath
            )
        return filePath
    except Exception as e:
        print("Error : ", e)

# Getter functions to retrieve iduser and passwd
def get_iduser():
    return iduser

def get_passwd():
    return passwd