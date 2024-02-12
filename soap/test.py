import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

def select_file():
    filetypes = (
        ('Text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/home/paul/Bureau/iatic5/services-web/',
        filetypes=filetypes)

    return filename

def return_selected_file():
    filePath = select_file()
    if filePath:
        showinfo(
            title='Selected File',
            message=filePath
        )
        return filePath

if __name__ == "__main__":
    filePath = return_selected_file()
    print(filePath)