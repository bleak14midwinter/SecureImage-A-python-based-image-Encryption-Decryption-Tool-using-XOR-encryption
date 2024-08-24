import tkinter as tk
from tkinter import filedialog, messagebox as mbox
from PIL import ImageTk, Image
import cv2
import numpy as np
import os
import shutil  

window = tk.Tk()
window.geometry("1800x950")
window.title("SecureImage")
window.configure(bg='black')


global count, eimg, image_encrypted, key, key_file, panelA, panelB
key_file = 'encryption_key.npy'  
panelA = None
panelB = None


image_encrypted = None
encrypted_image_path = None
key_path = None

def getpath(path):
    return os.path.dirname(path)

def getfilename(path):
    return os.path.splitext(os.path.basename(path))[0]

def openfilename():
    return filedialog.askopenfilename(title='Open')

def open_img():
    global x, panelA, panelB, eimg, resized_img, location, filename
    x = openfilename()
    if not x:
        return
    
    img = Image.open(x)
    max_width = 500  # Adjust as needed
    max_height = 500  # Adjust as needed
    img.thumbnail((max_width, max_height), Image.LANCZOS)
    
    # Save the resized image for encryption
    resized_img = img.copy()
    
    eimg = img
    img = ImageTk.PhotoImage(img)
    location = getpath(x)
    filename = getfilename(x)
    
    if panelA is None:
        panelA = tk.Label(window, image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
    else:
        panelA.configure(image=img)
        panelA.image = img

    if panelB is None:
        panelB = tk.Label(window, image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)
    else:
        panelB.configure(image=img)
        panelB.image = img



def en_fun():
    global resized_img, image_encrypted, key, panelB

    if resized_img is None:
        mbox.showerror("Error", "No image selected for encryption.")
        return

    image_input = np.array(resized_img.convert('L'))  # Convert to grayscale for encryption
    if image_input is None:
        mbox.showerror("Error", "Failed to process image.")
        return

    key = np.random.randint(0, 256, image_input.shape, dtype=np.uint8)

    image_encrypted = cv2.bitwise_xor(image_input, key)
    
    encrypted_image_path = 'image_encrypted.jpg'
    cv2.imwrite(encrypted_image_path, image_encrypted)

    np.save(key_file, key)  # Save the key

    imge = Image.open(encrypted_image_path)
    imge = ImageTk.PhotoImage(imge)
    
    if panelB is None:
        panelB = tk.Label(window, image=imge)
        panelB.image = imge
        panelB.pack(side="right", padx=20, pady=20)
    else:
        panelB.configure(image=imge)
        panelB.image = imge

    mbox.showinfo("Encrypt Status", "Image Encrypted successfully.")



# Declare image_output globally at the start
global image_output
image_output = None  # Initialize it to None

def de_fun():
    global image_encrypted, key, panelB, encrypted_image_path, image_output 

    if not encrypted_image_path:
        mbox.showerror("Error", "No encrypted image selected.")
        return

    if not os.path.exists(key_file):
        mbox.showerror("Error", "Encryption key file missing.")
        return

    key = np.load(key_file)

    encrypted_img = cv2.imread(encrypted_image_path, cv2.IMREAD_GRAYSCALE)
    if encrypted_img is None:
        mbox.showerror("Error", "Failed to load encrypted image.")
        return

    if key.shape != encrypted_img.shape:
        mbox.showerror("Error", "Key and encrypted image dimensions do not match.")
        return

    image_output = cv2.bitwise_xor(encrypted_img, key)  
    cv2.imwrite('image_output.jpg', image_output)

    imgd = Image.open('image_output.jpg')
    imgd = ImageTk.PhotoImage(imgd)

    if panelB is None:
        panelB = tk.Label(window, image=imgd)
        panelB.image = imgd
        panelB.pack(side="right", padx=20, pady=20)
    else:
        panelB.configure(image=imgd)
        panelB.image = imgd

    mbox.showinfo("Decrypt Status", "Image decrypted successfully.")


def download_decrypted_img():
    global image_output  # Use the global image_output variable

    if image_output is None:
        mbox.showwarning("No Image", "No decrypted image available to download.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    image_output_pil = Image.fromarray(image_output)
    if image_output_pil.mode == 'RGBA':
        image_output_pil = image_output_pil.convert('RGB')

    image_output_pil.save(file_path)
    mbox.showinfo("Success", "Decrypted Image Saved Successfully!")



def reset():
    global eimg, x, panelB

    if not x:
        mbox.showerror("Error", "No image selected to reset.")
        return

    # Load the original image
    image = Image.open(x)
    
    # Set the maximum width and height for the image
    max_width = 500  # Adjust this value as needed
    max_height = 500  # Adjust this value as needed

    # Resize the image to fit within the maximum dimensions
    image.thumbnail((max_width, max_height), Image.LANCZOS)
    
    eimg = image  # Store the resized image

    # Convert to ImageTk.PhotoImage for displaying in Tkinter
    image_tk = ImageTk.PhotoImage(image)

    if panelB is not None:
        panelB.configure(image=image_tk)
        panelB.image = image_tk
    else:
        panelB = tk.Label(window, image=image_tk)
        panelB.image = image_tk
        panelB.pack(side="right", padx=20, pady=20)
    
    mbox.showinfo("Success", "Image reset to original format!")

def save_img():
    global eimg

    if eimg is None:
        mbox.showwarning("No Image", "No image to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", 
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    if eimg.mode == 'RGBA':
        eimg = eimg.convert('RGB')

    eimg.save(file_path)
    mbox.showinfo("Success", "Image Saved Successfully!")
    
def download_encrypted_img():
    global image_encrypted

    if image_encrypted is None:
        mbox.showwarning("No Image", "No encrypted image available to download.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    image_encrypted_pil = Image.fromarray(image_encrypted)
    if image_encrypted_pil.mode == 'RGBA':
        image_encrypted_pil = image_encrypted_pil.convert('RGB')

    image_encrypted_pil.save(file_path)
    mbox.showinfo("Success", "Encrypted Image Saved Successfully!")  
    
def download_key():
    if not os.path.exists('encryption_key.npy'):
        mbox.showwarning("No Key", "No encryption key available to download.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".npy",
                                             filetypes=[("Numpy files", "*.npy"), ("All files", "*.*")])
    if not file_path:
        return

    shutil.copy('encryption_key.npy', file_path)
    mbox.showinfo("Success", "Encryption Key Saved Successfully!")  
    
def upload_encrypted_and_key():
    global encrypted_image_path, key_path, image_encrypted, key

    encrypted_image_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image files", "*.jpg;*.png")])
    if not encrypted_image_path:
        mbox.showwarning("No File", "No encrypted image selected.")
        return
    

    key_path = filedialog.askopenfilename(title="Select Encryption Key", filetypes=[("Numpy files", "*.npy")])
    if not key_path:
        mbox.showwarning("No File", "No key file selected.")
        return

    image_encrypted = cv2.imread(encrypted_image_path, cv2.IMREAD_GRAYSCALE).astype(float) / 255.0
    key = np.load(key_path)

    mbox.showinfo("Files Selected", "Encrypted image and key file selected successfully.")

    de_fun()  
    
def download_decrypted_img():
    global image_output

    if image_output is None:
        mbox.showwarning("No Image", "No decrypted image available to download.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
    if not file_path:
        return

    image_output_pil = Image.fromarray(image_output)
    if image_output_pil.mode == 'RGBA':
        image_output_pil = image_output_pil.convert('RGB')

    image_output_pil.save(file_path)
    mbox.showinfo("Success", "Decrypted Image Saved Successfully!")


# buttons 
start1 = tk.Label(text="SecureImage", font=("Arial", 40), fg="grey")
start1.place(x=600, y=10)

start1 = tk.Label(text="Original\nImage", font=("Arial", 40), fg="magenta")
start1.place(x=100, y=270)

start1 = tk.Label(text="Encrypted/\nDecrypted\nImage", font=("Arial", 40), fg="magenta")
start1.place(x=1150, y=230)

chooseb = tk.Button(window, text="Choose", command=open_img, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
chooseb.place(x=30, y=20)

saveb = tk.Button(window, text="Save", command=save_img, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
saveb.place(x=170, y=20)

enb = tk.Button(window, text="Encrypt", command=en_fun, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
enb.place(x=30, y=750)

deb = tk.Button(window, text="Decrypt", command=de_fun, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
deb.place(x=150, y=750)

resetb = tk.Button(window, text="Reset", command=reset, font=("Arial", 20), bg="yellow", fg="blue", borderwidth=3, relief="raised")
resetb.place(x=1400, y=750)

download_button = tk.Button(window, text="Download Enc. Img", command=download_encrypted_img, font=("Arial", 20), bg="light blue", fg="black", borderwidth=3, relief="raised")
download_button.place(x=272, y=750)

download_key_button = tk.Button(window, text="Download Key", command=download_key, font=("Arial", 20), bg="light pink", fg="black", borderwidth=3, relief="raised")
download_key_button.place(x=535, y=750)

upload_button = tk.Button(window, text="Upload Enc. Img and Key", command=upload_encrypted_and_key, font=("Arial", 20), bg="light blue", fg="black", borderwidth=3, relief="raised")
upload_button.place(x=740, y=750)

download_decrypted_button = tk.Button(window, text="Download Dec.", command=download_decrypted_img, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
download_decrypted_button.place(x=1100, y=750)

def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

exitb = tk.Button(window, text="EXIT", command=exit_win, font=("Arial", 20), bg="red", fg="blue", borderwidth=3, relief="raised")
exitb.place(x=1400, y=20)

window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()