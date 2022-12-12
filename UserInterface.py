import tkinter as tk
from tkinter import filedialog
import os
import AES

font = 'Helvetica'
heading = 16
subheading = 15
text = 14
mainBtnBg = '#447294'
secondaryBtn = '#AAB1C3'
bgcolor = '#dfcfd5'
textCol = '#3C4770'

window = tk.Tk()
#Setting Windows title
window.title('ViA Cryptography Course Work')
window.configure(bg=bgcolor)
# Setting window size
window.geometry("1400x900")
decryption = True
fileName = ''

# Creating text for user information
greeting = tk.Label(text="Hello, dear user. This is a program where you will be able to encrypt & decrypt your text files.", font=(font, heading), fg=textCol, bg=bgcolor)
info = tk.Label(text="You should choose the process - encryption or decryption, as well as the encryption standard.", font=(font, subheading), fg=textCol, bg=bgcolor)
# adding text to the window
greeting.pack(pady=30)
info.pack(pady=10)

# Change decription bool based on button clicked
def shouldDecrypt(value):
    global decryption
    print(value)
    decryption = value
    fileLabel = tk.Label(text="File selection", font=(font, 15), fg=textCol, bg=bgcolor)
    button_explore = tk.Button(
                        text = "Browse Files",
                        command = browseFiles, font=(font, 14), fg=bgcolor, bg=mainBtnBg)  
    fileLabel.pack(pady=20)
    button_explore.pack()

# Choice of process - encryption or decryption
choiceText = tk.Label(text="Would you like to ENCRYPT or DECRYPT your file?", font=(font, 15), fg=textCol, bg=bgcolor)
choiceText.pack(pady=50)
encryptBtn = tk.Button(text="Encrypt",command= lambda: shouldDecrypt(False), bg=mainBtnBg, fg=bgcolor, font=(font, 14))
decryptionBtn = tk.Button(text="Decrypt", command= lambda: shouldDecrypt(True), bg=secondaryBtn, font=(font, 14))
encryptBtn.place(x=600, y=230)
decryptionBtn.place(x=700, y=230)

# User choosing .txt file from their system
# Implementing file browser
def browseFiles():
    global fileName
    fileName = filedialog.askopenfilename(title = "Select a File", 
                                          filetypes = [("Text files","*.txt*")])
    fileName = os.path.abspath(fileName)
    fileLabel.configure(text="Opened file: " + fileName, bg=bgcolor, fg=textCol)

    # Creating buttons for different choices and method calling
    choiceText = tk.Label(text="Would you like to use AES or DES encryption standard?", font=(font, 14), fg=textCol, bg=bgcolor)
    choiceText.pack(pady=20)
    aesBtn = tk.Button(text="AES", bg=mainBtnBg, fg=bgcolor, command = lambda: run('AES.py'), font=(font, 14))
    desBtn = tk.Button(text="DES",bg=secondaryBtn, command = lambda: run('DES.py'), font=(font, 14))
    aesBtn.place(x=620, y=450)
    desBtn.place(x=720, y=450)

fileLabel = tk.Label(text='')

button_exit = tk.Button(
                     text = "Exit",
                     command = exit, font=(font, 14))
button_exit.pack()
button_exit.place(x=1300, y=20)

# Script running function
def run(file):
    choiceText.configure(text="chosen file for running: "+ file, bg=bgcolor, fg=textCol, font=(font, 13))
    os.system(file)

    # Implementing key input fields
    initVector = tk.Entry(text="Please enter your initialization vector ", font=(font, 13), fg=textCol)
    initVector.pack(pady=65)



window.mainloop()

