from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano import lsb  # pip install stegano

root = Tk()

root.title("Steganography - Hide a secret Text Message in an Image")
root.geometry("700x500+250+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

filename = None  # Define a global variable to store the file path

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',
                                           filetypes=(("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")))

    if filename:
        img = Image.open(filename)
        img = img.resize((250, 250))  # Resize to fit the label
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

def Hide():
    global filename
    message = text1.get(1.0, END)
    
    if filename and message.strip():
        secret = lsb.hide(str(filename), message)
        secret.save("hidden.png")
    else:
        print("No image selected or message is empty")

def Show():
    global filename
    if filename:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    else:
        print("No image selected")

def save():
    global filename
    if filename:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            secret = lsb.hide(str(filename), text1.get(1.0, END))
            secret.save(save_path)
    else:
        print("No image selected")

# icon
image_icon = PhotoImage(file="logo.jpg")
root.iconphoto(False, image_icon)

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text='CYBER SCIENCE', bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first Frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

# second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save).place(x=180, y=30)

Label(frame3, text="Picture, Image, Photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

# Fourth Frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)

Label(frame4, text="Picture, Image, Photo file", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
