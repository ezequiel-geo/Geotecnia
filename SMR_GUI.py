from tkinter import *
from PIL import ImageTk, Image
from math import *

root = Tk()
root.title("SMR (Romana, 2001)")
root.geometry("800x500")

intro = Label(root,text="Ingresar el RMRb y luego indicar la orientación de la familia de discontinuidad y talud. Calcular el SMR para cada familia y adoptar el menor valor.", font=("", "8", "bold"))
intro.place(x=10, y=10)

#Ingresar los parámetros del macizo y talud
rmr=Label(root, text="Ingrese RMRb")
rmr.place(x=10, y=40)

rmrb=Entry(root)
rmrb.place(x=100, y=40, width=22)

dir_disc = Label(root, text="Dirección de inclinación de la familia de discontinuidades")
dir_disc.place(x=10, y=80)
dir_disce = Entry(root)
dir_disce.place(x=380, y=80, width=30)

incl_disc = Label(root, text="Inclinación de la familia de discontinuidades")
incl_disc.place(x=10, y=120)
incl_disce = Entry(root)
incl_disce.place(x=380, y=120, width=30)

dir_intersecc = Label(root, text="Dir. de inclinación de la intersección de dos discontinuidades*")
dir_intersecc.place(x=10, y=160)
dir_intersecce = Entry(root)
dir_intersecce.place(x=380, y=160, width=30)

incl_intersecc = Label(root, text="Buzamiento de la intersección de dos discontinuidades*")
incl_intersecc.place(x=10, y=200)
incl_intersecce = Entry(root)
incl_intersecce.place(x=380, y=200, width=30)

dir_talud = Label(root, text="Dirección de inclinación del talud")
dir_talud.place(x=10, y=240)
dir_talude = Entry(root)
dir_talude.place(x=380, y=240, width=30)

incl_talud = Label(root, text="Inclinación del talud")
incl_talud.place(x=10, y=280)
incl_talude = Entry(root)
incl_talude.place(x=380, y=280, width=30)

nota = Label(root, text="* solo para rotura en cuña", font=("","7", "bold"))
nota.place(x=10, y=320)

#Flechas y botones
canvas = Canvas(root)
canvas.place(x=425, y=70)
canvas.create_line(0, 120, 50, 120, arrow=LAST)

f1 = Label(root, text="F1=").place(x=650, y = 100)
f2 = Label(root, text="F2=").place(x=650, y = 140)
f3 = Label(root, text="F3=").place(x=650, y = 180)
f4 = Label(root, text="F4=").place(x=650, y = 220)
smr = Label(root, text="SMR=", font = ("", "10", "bold")).place(x=640, y = 260)
f1_ = Entry(root)
f1_.place(x=700, y = 100, width=30)

def rot_plana():
    f1r = round((1 - sin (abs(int(dir_disce.get())-int(dir_talude.get()))))**2,2)
    f1_.insert(0,f1r)
    return


def clear():
    f1_.delete(0,END)

plana = Button(root, text="Rotura plana", command = rot_plana)
plana.place(x=500, y=140)

vuelco = Button(root, text="Vuelco")
vuelco.place(x=500, y=180)

cuña = Button(root, text="Rotura en cuña")
cuña.place(x=500, y=220)

borrar = Button(root, text="Nuevo cálculo", command = clear)
borrar.place(x=600, y=400)



root.mainloop()
