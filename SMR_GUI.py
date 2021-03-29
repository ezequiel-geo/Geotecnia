import tkinter
from tkinter import * 
import tkinter as tk
from PIL import ImageTk, Image
import math
from math import *

root = Tk()
root.title("SMR (Romana, 2001)")
root.geometry("800x500")

intro = Label(root,text="Ingresar todos los valores a la izquierda (los items con * solo si es rotura por cuña).Luego, elegir el modo de deslizamiento.", font=("", "8", "bold"))
intro.place(x=10, y=10)

#Ingresar los parámetros del macizo y talud
rmr=Label(root, text="RMRb")
rmr.place(x=10, y=40)

rmrb=Entry(root)
rmrb.place(x=380, y=40, width=30)

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

variable = StringVar()
variable.set("Seleccionar")
variable_ = variable.get()

def exca(variable_):
    if variable_ == "Talud natural":
        f4_.insert(0, "15")
    if variable_ == "Precorte":
        f4_.insert(0, "10")
    if variable_ == "Voladura suave":
        f4_.insert(0, "8")
    if variable_ == "Voladura o mecánica":
        f4_.insert(0, "0")
    if variable_ == "Voladura deficiente":
        f4_.insert(0, "-8")
    return

exc = Label(root, text="Método de excavación")
exc.place(x=10, y=320)
exce = OptionMenu(root, variable, "Talud natural", "Precorte", "Voladura suave", "Voladura o mecánica", "Voladura deficiente", command=exca).place(x=320, y=320)


nota = Label(root, text="* solo para rotura en cuña", font=("","7", "bold"))
nota.place(x=10, y=360)


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
f2_ = Entry(root)
f2_.place(x=700, y = 140, width=30)
f3_ = Entry(root)
f3_.place(x=700, y = 180, width=30)
f4_ = Entry(root)
f4_.place(x=700, y = 220, width=30)
smr_ = Entry(root)
smr_.place(x=700, y = 260, width=30)

def rot_plana():
    a = math.radians(int(dir_disce.get())-int(dir_talude.get()))
    f1r = round((1 - sin (abs(a)))**2,2)
    f1_.insert(0,f1r)
    b = math.radians(int(incl_disce.get()))
    f2r= round((tan(b))**2,2)
    f2_.insert(0,f2r)
    c = int(incl_disce.get())
    d = int(incl_talude.get())
    f3r = round(c-d,2)
    f3_.insert(0,f3r)
    smr_p = int(rmrb.get()) + (f1r)*(f2r)*(f3r) +int(f4_.get())
    smr_.insert(0,smr_p)
    return

def rot_vuelco():
    a = math.radians(int(dir_disce.get())-int(dir_talude.get())-1.57)
    f1rv = round((1 - sin (abs(a)))**2,2)
    f1_.insert(0,f1rv)
    b = math.radians(int(incl_disce.get()))
    f2rv= round((tan(b))**2,2)
    f2_.insert(0,f2rv)
    c = int(incl_disce.get())
    d = int(incl_talude.get())
    f3rv = round(c+d,2)
    f3_.insert(0,f3rv)
    smr_v = int(rmrb.get()) + (f1rv)*(f2rv)*(f3rv)+int(f4_.get())
    smr_.insert(0,smr_v)
    return

def rot_cuña():
    a = math.radians(int(dir_intersecce.get())-int(dir_talude.get())-1.57)
    f1rc = round((1 - sin (abs(a)))**2,2)
    f1_.insert(0,f1rc)
    b = math.radians(int(incl_intersecce.get()))
    f2rc= round((tan(b))**2,2)
    f2_.insert(0,f2rc)
    c = int(incl_intersecce.get())
    d = int(incl_talude.get())
    f3rc = round(c-d,2)
    f3_.insert(0,f3rc)
    smr_c = int(rmrb.get()) + (f1rc)*(f2rc)*(f3rc)+int(f4_.get())
    smr_.insert(0,smr_c)
    return


def clear():
    f1_.delete(0,END)
    f1_.forget()
    f2_.delete(0,END)
    f2_.forget()
    f3_.delete(0,END)
    f3_.forget()
    f4_.delete(0,END)
    f4_.forget()
    smr_.delete(0,END)
    smr_.forget()

plana = Button(root, text="Rotura plana", command = rot_plana)
plana.place(x=500, y=140)

vuelco = Button(root, text="Vuelco", command= rot_vuelco)
vuelco.place(x=500, y=180)

cuña = Button(root, text="Rotura en cuña", command= rot_cuña)
cuña.place(x=500, y=220)

borrar = Button(root, text="Nuevo cálculo", command = clear)
borrar.place(x=600, y=400)

root.mainloop()
