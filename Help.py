from cgitb import text
from tkinter import*
from tkinter import ttk
from turtle import bgcolor, width
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector as mc
import cv2
class Help:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1250x700') #self.root.geometry('1400x800')
        self.root.title("Face recognition")

        title_lbl=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg ="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_left = Image.open(r"D:\projects\Smart Attendance\437.jpg")
        img_left = img_left.resize((710, 720), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0, y=55, width=715, height=720)

        dev_lbl = Label(f_lbl, text="Guidelines",
                        font=("Montserrat", 20, "bold"), bg="#CBEDD5")
        dev_lbl.place(x=380, y=30)
        
        img_right = Image.open(r"D:\projects\Smart Attendance\437.jpg")
        img_right = img_right.resize((715, 720), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=713, y=55, width=715, height=720)

        dev_lbl = Label(f_lbl, text="Contact Us",font=("Montserrat", 20, "bold"), bg="#CBEDD5")
        dev_lbl.place(x=20, y=30)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()        