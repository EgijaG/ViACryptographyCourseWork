import tkinter as tk
window = tk.Tk()

# Creating text for user information
greeting = tk.Label(text="Hello, dear user. This is a program where you will be able to encrypt & decrypt your text files.")
info = tk.Label(text="You should choose the process - ENCRYPT or DECRYPT and encryption standard.")
# adding text to the window
greeting.pack()
info.pack()

# Setting window size
window.geometry("800x600")

# Choice of process - encryption or decryption
choiceText = tk.Label(text="Would you like to ENCRYPT or DECRYPT your file?")
choiceText.pack()
encryptBtn = tk.Button(text="Encrypt", bg='green')
decryptionBtn = tk.Button(text="Decrypt", bg='purple')
encryptBtn.pack()
decryptionBtn.pack()
# Creating buttons for different choices and method calling

# Implementing file browser

# Implementing key input fields





window.mainloop()
