from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Q (Barton, 1974)")
root.geometry("1275x1200")

#Introducción al programa
label = Label(root, text="Para clasificar el macizo rocoso según la clasificación Q, utilizar la tabla de la derecha para")
label2 = Label(root, text="asignar un puntaje a cada parámetro. Luego, utilizar la corrección por tipo de obra y")
label3 = Label(root, text="orientación de las discontinuidades, de ser necesario.")
label.place(x=0,y=0)
label2.place(x=0,y=17)
label3.place(x=0,y=35)

#Parámetros, puntajes y referencia
label_ref = Label(root, text="González de Vallejo, L.I. 2002. Ingeniería geológica. Pearson Education.")
label_ref.place(x=880, y=750)

r1= Image.open("RMR.jpg")     
r2 = r1.resize((750, 750), Image.ANTIALIAS)
r3 = ImageTk.PhotoImage(r2)
rmr_1 = Label(image=r3)
rmr_1.place(x=500, y=0)

#Entrada de puntajes, boton para calcular el final

p1 = Entry(root)
p1.place(x=300, y=100, width=25)
p1l = Label(root,text="Jr")
p1l.place(x=50, y=100)

p2 = Entry(root)
p2.place(x=300, y=150, width=25)
p2l = Label(root,text="RQD (%)")
p2l.place(x=125, y=150)

p3 = Entry(root)
p3.place(x=300, y=200, width=25)
p3l = Label(root,text="Ja")
p3l.place(x=75, y=200)

p4 = Entry(root)
p4.place(x=300, y=250, width=25)
p4l = Label(root,text="Jw")
p4l.place(x=125, y=250)

p5 = Entry(root)
p5.place(x=300, y=300, width=25)
p5l = Label(root,text="Jn")
p5l.place(x=125, y=300)

p6 = Entry(root)
p6.place(x=300, y=350, width=25)
p6l = Label(root,text="SRF")
p6l.place(x=125, y=350)

q = Entry(root)
q.place(x=300, y=650, width=25)
q_ = Entry(root)
q_.place(x=325, y=650, width=160)


def calculo():
    global q
    q=int(p1.get()) + int(p2.get()) + int(p3.get()) + int(p4.get()) + int(p5.get()) + int(p6.get()) + int(p7.get()) + int(p8.get()) + int(p9.get()) + int(correccion.get())
    rmrb.insert(0,rmr)
    if rmr>=81:
        rmrc.insert(0, "Clase I - Calidad muy buena")
    elif rmr<=80 and rmr>=61:
        rmrc.insert(0,"Clase II - Calidad buena")
    elif rmr<=60 and rmr>=41:
        rmrc.insert(0,"Clase III - Calidad media")
    elif rmr<=40 and rmr>=21:
        rmrc.insert(0,"Clase IV - Calidad mala")
    else:
        rmrc.insert(0,"Clase V - Calidad muy mala")
    
def borrar(): #borrar contenido para nuevo calculo
    rmrb.delete(0,END)
    rmrc.delete(0,END)

calcular = Button(root, text="Calcular RMR", padx=10, pady=10, command= calculo)
calcular.place(x=120, y=650)

borrar = Button(root, text="Borrar", padx=10, pady=10, command= borrar)
borrar.place(x=125, y=700)

root.mainloop() 
