from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Q (Barton, 1974)")
root.geometry("750x750")

#Introducción al programa
label = Label(root, text="Clasificar del macizo rocoso según la clasificación Q. Clickear en los botones ! para información:", font=("", "12"))
label.place(x=0,y=0)

#Parámetros
#Parámetro RQD
rqd = Label(root, text="RQD (%)", font=("","11")) 
rqd.place(x=5, y=50)
rqd_ = Entry(root, width=5)
rqd_.place(x=75, y=50)

#Parámetro Jn
def Jn():
    jn1=Tk()
    jn1.title("Jn")
    jn1.geometry("750x750+750+50")
    jn2= Image.open("jn.jpg")     
    jn3 = ImageTk.PhotoImage(jn2)
    jn4 = Label(jn1, image=jn3)
    jn4.place(x=10, y=10)
    return

jn = Label(root, text="Jn", font=("","11")) 
jn.place(x=15, y=90)
jn_ = Entry(root, width=5)
jn_.place(x=75, y=90)
jn__ = Button(root, text="!", width=5, command=Jn)
jn__.place(x=120, y=87)



root.mainloop() 
