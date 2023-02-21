import tkinter as tk
from tkinter import filedialog
import shutil
import os

class FileCopyApp:
    def __init__(self, master):
        self.master = master
        master.title("File Copy App")
        master.geometry("400x380")

        # create the select file button
        self.select_file_button = tk.Button(master, text="Select File", command=self.select_file)
        self.select_file_button.pack(pady=10)

    def select_file(self):
        # open a file dialog to select a file
        file_path = filedialog.askopenfilename()

        # create the copy file button and path button
        self.copy_file_button = tk.Button(self.master, text="Copy File", command=lambda: self.copy_file(file_path))
        self.copy_file_button.pack(pady=10)

        self.path_button = tk.Button(self.master, text="Select Destination Path", command=self.select_path)
        self.path_button.pack(pady=5)

    def select_path(self):
        # open a file dialog to select a destination path
        dest_path = filedialog.askdirectory()

        # update the text of the path button
        self.path_button.configure(text="Destination Path: {}".format(dest_path))

        # save the destination path for later use
        self.dest_path = dest_path

    def copy_file(self, file_path):
        # copy the file to the destination path
        shutil.copy(file_path, self.dest_path)

        # display a success message
        success_message = tk.Label(self.master, text="File copied successfully to {}".format(self.dest_path))
        success_message.pack(pady=10)
root = tk.Tk()
app = FileCopyApp(root)
root.mainloop()
