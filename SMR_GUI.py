from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("SMR (Romana, 2001)")
root.geometry("800x500")

intro = Label(root,text="Ingresar el RMRb y luego indicar la orientación de la familia de discontinuidad y talud. Calcular el SMR para cada familia y adoptar el menor valor.")
intro.place(x=10, y=10)

rmr=Label(root, text="Ingrese RMRb")
rmr.place(x=10, y=40)

rmrb=Entry(root)
rmrb.place(x=100, y=40, width=22)

dir_disc = Label(root, text="Dirección de inclinación de las discontinuidades")
dir_disc.place(x=10, y=80)
dir_disce = Entry(root)
dir_disce.place(x=300, y=80, width=30)

incl_disc = Label(root, text="Inclinación de las discontinuidades")
incl_disc.place(x=10, y=120)
incl_disce = Entry(root)
incl_disce.place(x=300, y=120, width=30)

dir_talud = Label(root, text="Dirección de inclinación del talud")
dir_talud.place(x=10, y=160)
dir_talude = Entry(root)
dir_talude.place(x=300, y=160, width=30)

incl_talud = Label(root, text="Inclinación del talud")
incl_talud.place(x=10, y=200)
incl_talude = Entry(root)
incl_talude.place(x=300, y=200, width=30)

canvas = Canvas(root)
canvas.place(x=400, y=150)
canvas.create_line(410, 100, 430, 150, arrow=LAST)  

root.mainloop()
