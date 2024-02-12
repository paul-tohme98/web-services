import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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