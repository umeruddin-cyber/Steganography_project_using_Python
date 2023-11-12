import cv2
import os
import string
import tkinter as tk
from tkinter import filedialog, messagebox

# Define global variables
img = None
media_data = ""
password = ""
c = {}

# Function to load image or text file
def load_media():
    global img, media_data
    file_path = filedialog.askopenfilename()

    _, file_extension = os.path.splitext(file_path.lower())
    
    if file_extension in {'.jpg', '.jpeg', '.png'}:
        img = cv2.imread(file_path)
        media_data = ""
        messagebox.showinfo("Success", "Image loaded successfully.")
    elif file_extension == '.txt':
        with open(file_path, 'r') as file:
            media_data = file.read()
        img = None
        messagebox.showinfo("Success", "Text file loaded successfully.")
    else:
        messagebox.showwarning("Warning", "Unsupported file type. Please select an image (.jpg, .jpeg, .png) or text (.txt) file.")

# Function to encrypt media data
def encrypt_message():
    global media_data, img

    # Check if media data is provided
    if not media_data:
        messagebox.showwarning("Warning", "No media data provided.")
        return

    if img is not None:
        # Convert media data to a list of integers for encryption
        data_to_encrypt = [ord(char) for char in media_data]

        # Loop through the media data and encrypt
        n, m, z = 0, 0, 0

        for i in range(len(data_to_encrypt)):
            img[n, m, z] = data_to_encrypt[i]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3

        # Save the modified media file
        cv2.imwrite("EncryptedMedia.jpg", img)

        messagebox.showinfo("Success", "Encryption completed. Encrypted media saved as 'EncryptedMedia.jpg'.")
    else:
        messagebox.showwarning("Warning", "No image loaded.")

# Function to decrypt media data
def decrypt_message():
    global password, img, c

    pas = entry_passcode.get()

    if password == pas:
        if img is not None:
            message = ""
            n, m, z = 0, 0, 0

            for i in range(len(media_data)):
                message = message + c[img[n, m, z]]
                n = n + 1
                m = m + 1
                z = (z + 1) % 3
            messagebox.showinfo("Decryption", f"Decryption message:\n{message}")
        else:
            messagebox.showwarning("Warning", "No image loaded.")
    else:
        messagebox.showwarning("Invalid Key", "Not a valid key.")

# GUI
root = tk.Tk()
root.title("Media Steganography")
root.iconbitmap("E://Desktop//IBM Internship//OpenStego//img//image locking.ico")

# UI components
label_msg = tk.Label(root, text="Enter secret message:")
entry_msg = tk.Entry(root)

label_password = tk.Label(root, text="Enter password:")
entry_password = tk.Entry(root, show="*")

btn_load_media = tk.Button(root, text="Load Media", command=load_media)
btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_message)

label_passcode = tk.Label(root, text="Enter passcode for Decryption:")
entry_passcode = tk.Entry(root, show="*")
btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_message)

# Arrange UI components
label_msg.pack()
entry_msg.pack()

label_password.pack()
entry_password.pack()

btn_load_media.pack()
btn_encrypt.pack()

label_passcode.pack()
entry_passcode.pack()

btn_decrypt.pack()

# Run the GUI
root.mainloop()
