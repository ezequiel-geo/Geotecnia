#Script en Python para clasificar macizos rocosos según el sistema RMR (Rock Mass Rating de Bienawski, 1989). El RMR obtenido es 
# el básico, RMRb, al que luego puede modificar con otras clasificaciones complementarias (por ejemplo, SMR de Romana para taludes)


print("Bienvenido a mi script realizado en Python para clasificar macizos rocosos según el sistema RMR (Rock Mass Rating de Bienawski, 1989)")
print("Ir escribiendo los puntajes para cada parámetro, al f inal se puede realizar una adecuación según el tipo de obra.")

#Primero se definen los 5 parámetros del RMRb. Luego, se da la opción de adecuarlos:

def parametro_1():
    print("Resistencia de la matriz rocosa (MPa):")
    resistencia = input("Ingrese el tipo de ensayo, (c)arga puntual o compresión (s)imple")
    if resistencia == "c":
        print("Puntaje - Valor del ensayo de carga puntual")
        print("15          >10")
        print("12          10-4")
        print("7           4-2")
        print("4           2-1")
        print("Para valores menores a 1, utilizar el ensayo de compresión simple")
        p1c = input("Ingrese puntaje adoptado:")
        return(p1c)
    else:
        print("Puntaje - Valor del ensayo de compresión simple (MPa)")
        print("15          >250")
        print("12          250-100")
        print("7           100-50")
        print("4           50-25")
        print("2           25-5")
        print("1           5-1")
        print("0           <1")
        p1s = input("Ingrese puntaje adoptado:")
        return(p1s)


def parametro_2():
    print("RQD (%):")
    print("Puntaje - RQD")
    print("20          90-100")
    print("17          90-75")
    print("13          75-50")
    print("6           50-25")
    print("3           <25")
    p2 = input("Ingrese puntaje adoptado:")
    return(p2)  
  
def parametro_3():
    print("Separación entre diaclasas (m):")
    print("Puntaje - Separación entre diaclasas")
    print("20          >2")
    print("15          2-0.6")
    print("10          0.6-0.2")
    print("8           0.2-0.06")
    print("5           <0.06")
    p3 = input("Ingrese puntaje adoptado:")
    return(p3)  

def parametro_4():
    print("Estado de las discontinuidades:")
    print("Puntaje - Persistencia (m)")
    print("6           <1")
    print("4           1-3")
    print("2           3-10")
    print("1           10-20")
    print("0           >20")
    p4a = input("Ingrese puntaje adoptado:")
    print("Puntaje - Abertura (mm)")
    print("6           Nada")
    print("5           <0.1")
    print("3           0.1-1")
    print("1           1-5")
    print("0           >5")
    p4b = input("Ingrese puntaje adoptado:")
    print("Puntaje - Rugosidad")
    print("6           Muy rugosa")
    print("5           Rugosa")
    print("3           Ligeramente rugosa")
    print("1           Ondulada")
    print("0           Suave")
    p4c = input("Ingrese puntaje adoptado:")
    print("Puntaje - Alteración")
    print("6           Inalterada")
    print("5           Ligeramente alterada")
    print("3           Moderadamente alterada")
    print("1           Muy alterada")
    print("0           Descompuesta")
    p4d = input("Ingrese puntaje adoptado:")
    print("Puntaje - Relleno")
    print("6           Ninguno")
    print("4           Duro y <5mm")
    print("2           Duro y >5mm")
    print("2           Blando y <5mm")
    print("0           Blando y >5mm")
    p4e = input("Ingrese puntaje adoptado:")
    p4 = int(p4a)+int(p4b)+int(p4c)+int(p4d)+int(p4e)
    return(p4)

def parametro_5():
    print("Agua freática:")
    agua_freatica = input("Ingrese el método de evaluación, (c)audal por 10m de tunel, (r)elación entre presión de agua y tensión principal mayor o (e)stado general del macizo")
    if agua_freatica == "c":
        print("Puntaje - Valor del caudal por 10m de tunel (lt/min)")
        print("15          Nulo")
        print("10          <10")
        print("7           10-25")
        print("4           25-125")
        print("0           >125")
        p5c = input("Ingrese puntaje adoptado:")
        return(p5c)
    elif agua_freatica == "r":
        print("Puntaje - Valor de la relación presión de agua-tensión principal mayor")
        print("15          0")
        print("10          0-0.1")
        print("7           0.1-0.2")
        print("4           0.2-0.5")
        print("0           >0.5")
        p5r = input("Ingrese puntaje adoptado:")
        return(p5r)
    else:
        print("Puntaje - Estado general del macizo")
        print("15          Seco")
        print("10          Ligeramente húmedo")
        print("7           Húmedo")
        print("4           Goteando")
        print("0           Agua fluyendo")
        p5e = input("Ingrese puntaje adoptado:")
        return(p5e)

c = int(parametro_1()) + int(parametro_2()) + int(parametro_3()) + int(parametro_4()) + int(parametro_5())
print("El RMRb del macizo es:", c)

def clase_macizo():
    if c>=81:
        print("Clase I - Calidad muy buena")
    elif c<=80 and c>=61:
        print("Clase II - Calidad buena")
    elif c<=60 and c>=41:
        print("Clase III - Calidad media")
    elif c<=40 and c>=21:
        print("Clase IV - Calidad mala")
    else:
        print("Clase V - Calidad muy mala")

clase_macizo()

adecuar = input("Desea adecuar el RMRb de acuerdo al tipo de obra y orientación de las discontinuidades? (s)i o (n)?")

def adecuacion():
    if adecuar == "n":
        print()
    else:
        obra = input("Defina el tipo de obra: (t)unel, (f)undaciones o (ta)ludes [NOTA: para taludes, se recomienda utilizar la clasificación SMR de Roamana]")
        orientacion_discont = input("Defina, según rumbo e inclinación de las discontinuidades, si la orientación es (m)uy favorable, (f)avorable, (me)dia, (d)esfavorable o (mu)y desfavorable")
        global c
        if obra == "t" and orientacion_discont == "m":
            c = c - 0
        elif obra == "t" and orientacion_discont == "f":  
            c = c - 2
        elif obra == "t" and orientacion_discont == "me":  
            c = c - 5
        elif obra == "t" and orientacion_discont == "d":  
            c = c - 10
        elif obra == "t" and orientacion_discont == "mu": 
            c = c - 12 
        elif obra == "f" and orientacion_discont == "m":
            c = c - 0
        elif obra == "f" and orientacion_discont == "f":  
            c = c - 2
        elif obra == "f" and orientacion_discont == "me":  
            c = c - 7
        elif obra == "f" and orientacion_discont == "d":  
            c = c - 15
        elif obra == "f" and orientacion_discont == "mu": 
            c = c - 25 
        elif obra == "ta" and orientacion_discont == "m":
            c = c - 0
        elif obra == "ta" and orientacion_discont == "f":  
            c = c - 5
        elif obra == "ta" and orientacion_discont == "me":  
            c = c - 25
        elif obra == "ta" and orientacion_discont == "d":  
            c = c - 50
        else: 
            c = c - 60     
        print("El RMRb del macizo es:", c)
        clase_macizo()

adecuacion()

de_nuevo = input("Desea volver a clasificar el macizo? (s)i o (n)o?")

while de_nuevo == "s":
    c = int(parametro_1()) + int(parametro_2()) + int(parametro_3()) + int(parametro_4()) + int(parametro_5())
    print("El RMRb del macizo es:", c)
    clase_macizo()
    adecuacion()
    de_nuevo = input("Desea volver a clasificar el macizo? (s)i o (n)o?")