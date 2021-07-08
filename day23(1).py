# Basic Image converter App
# Create a browse option with a specific folder which has all the JPEG Files
# Create a Convert button to convert the image from JPEG to PNG

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=550, height=550, bg='Black', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Conversion From JPEG To PNG', bg='Green2', fg='White')
label1.config(font=('helvetica', 20))
canvas1.create_window(250, 40, window=label1)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='Red2', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='Dark Orange', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)

root.mainloop()