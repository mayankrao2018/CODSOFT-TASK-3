import random
import string
import pyperclip
from tkinter import *

# Initialize the Tkinter window
root = Tk()
root.geometry("400x400")  # Set the window size
root.title("Random Password Generator")  # Set the window title

# Create a label for password length
pass_head = Label(root, text='Password Length', font='arial 12 bold')
pass_head.pack(pady=10)

# Create a spinbox to select the password length
pass_len = IntVar()  # Integer variable to store the input length
length = Spinbox(root, from_=4, to_=32, textvariable=pass_len, width=24, font='arial 16')
length.pack()

# Function to generate a random password
def randPassGen():
    length = pass_len.get()  # Get the desired password length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)  # Copy the password to clipboard
    print(f"Generated Password: {password}")

# Create a button to generate the password
generate_button = Button(root, text="Generate Password", command=randPassGen)
generate_button.pack(pady=10)

root.mainloop()  # Start the GUI event loop
