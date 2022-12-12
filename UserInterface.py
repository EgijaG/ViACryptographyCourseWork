import tkinter as tk
from tkinter import filedialog
import os
from AES import *
import DES_encryption
import FileOperations
window = tk.Tk()
aes = AES()

decryption = True
algorithm = 1   #0 - DES, 1 - AES
fileName = ''

# Creating text for user information
greeting = tk.Label(text="Hello, dear user. This is a program where you will be able to encrypt & decrypt your text files.")
info = tk.Label(text="You should choose the process - ENCRYPT or DECRYPT and encryption standard.")
# adding text to the window
greeting.pack()
info.pack()

#Setting Windows title
window.title('ViA Cryptography Course Work')

# Setting window size
window.geometry("1400x1000")

# Change decription bool based on button clicked
def shouldDecrypt(value):
    global decryption
    print(value)
    decryption = value
    fileLabel = tk.Label(text="File selection")
    button_explore = tk.Button(
                        text = "Browse Files",
                        command = browseFiles)  
    fileLabel.pack()
    button_explore.pack()

# Choice of process - encryption or decryption
choiceText = tk.Label(text="Would you like to ENCRYPT or DECRYPT your file?")
choiceText.pack()
encryptBtn = tk.Button(text="Encrypt", bg='green' ,command= lambda: shouldDecrypt(False))
decryptionBtn = tk.Button(text="Decrypt", bg='purple', command= lambda: shouldDecrypt(True))
encryptBtn.pack()
decryptionBtn.pack()

# User choosing .txt file from their system
# Implementing file browser
def browseFiles():
    global fileName
    fileName = filedialog.askopenfilename(title = "Select a File",
                                          filetypes = [("Text files","*.txt*")])
    
    fileName = os.path.abspath(fileName)
    fileLabel.configure(text="Opened file: " + fileName)

    # Creating buttons for different choices and method calling
    choiceText = tk.Label(text="Would you like to use AES or DES encryption standard?")
    choiceText.pack()
    aesBtn = tk.Button(text="AES", bg='blue', command = lambda: run('AES.py'))
    desBtn = tk.Button(text="DES", bg='grey', command = lambda: run('DES.py'))
    aesBtn.pack()
    desBtn.pack()

fileLabel = tk.Label(text='')

button_exit = tk.Button(
                     text = "Exit",
                     command = exit)
button_exit.pack()
button_exit.place(x=1300, y=20)

#Key generation function
def generateCryptoKey():
    global algorithm
    plainText = FileOperations.readFileContent(fileName)
    print(algorithm)
    if algorithm == 0:
        key = DES_encryption.createRoundKeys('asdasdasasdasdasasdasdasasdasdasasdasdasasdasdasasdasdas', False)
        result = tk.Label(text=key)
        result.pack()
    else:
        key = ''
        cipherText = ''
        cipher = aes.encrypt(plainText, AES.KeyInfo.SMALL)
        for block in cipher.finalKey.list:
            for value in block:
                key += hex(value).lstrip('0x')
        FileOperations.writeContentToFile(key, 'aes.key')
        print(cipher.cipheredTextBlocks.list)
        for block in cipher.cipheredTextBlocks.list:
            for col in block.list:
                for value in col:
                    cipherText += hex(value).lstrip('0x')
        FileOperations.writeContentToFile(key, 'secret.txt')

# Script running function
def run(file):
    choiceText.configure(text="chosen file for running: "+ file)
    #os.system(file)

    encryptButton = tk.Button(text='Generate key', command= generateCryptoKey)
    encryptButton.pack()
    # Implementing key input fields
    #initVector = tk.Entry(text="Please enter your initialization vector ")
    #initVector.pack()



window.mainloop()

