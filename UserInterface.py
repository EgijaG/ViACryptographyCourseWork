import tkinter as tk
from tkinter import filedialog
import os
window = tk.Tk()

decryption = True
fileName = ''

# Creating text for user information
greeting = tk.Label(text="Hello, dear user. This is a program where you will be able to encrypt & decrypt your text files.")
info = tk.Label(text="You should choose the process - ENCRYPT or DECRYPT and encryption standard.")
# adding text to the window
greeting.pack()
info.pack()

# Setting window size
window.geometry("1400x1000")

# Choice of process - encryption or decryption
choiceText = tk.Label(text="Would you like to ENCRYPT or DECRYPT your file?")
choiceText.pack()
encryptBtn = tk.Button(text="Encrypt", bg='green')
decryptionBtn = tk.Button(text="Decrypt", bg='purple')
encryptBtn.pack()
decryptionBtn.pack()

# User choosing .txt file from their system
# Implementing file browser
def browseFiles():
    filename = filedialog.askopenfilename(title = "Select a File",
                                          filetypes = [("Text files","*.txt*")])
    global fileName
    fileName = os.path.abspath(filename)
    fileLabel.configure(text="Opened file: " + filename)

fileLabel = tk.Label(text="File selection")
button_explore = tk.Button(
                        text = "Browse Files",
                        command = browseFiles)  
button_exit = tk.Button(
                     text = "Exit",
                     command = exit)
fileLabel.pack()
button_explore.pack()
button_exit.pack()

# Script running function
def run(filename):
    choiceText.configure(text="chosen file for running: "+ filename)
    os.system(filename)
# Creating buttons for different choices and method calling
choiceText = tk.Label(text="Would you like to use AES or DES encryption standard?")
choiceText.pack()
aesBtn = tk.Button(text="AES", bg='blue', command = run('AES.py'))
desBtn = tk.Button(text="DES", bg='grey', command = run('DES.py'))
aesBtn.pack()
desBtn.pack()

# Implementing key input fields



window.mainloop()
