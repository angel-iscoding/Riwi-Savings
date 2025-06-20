import os

def clear(): 
    os.system("clear")

def menu (msj: str):
    clear()

    chars = [" ", "⎢", "⎥", "∙", "⎯"]
    
    #Separa el mensaje dentro de una lista
    separed = msj.splitlines()
    
    #Tamaño del menu
    size = 100

    #Head del menu
    menu = f"{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    #Bucle para recorrer la lista
    for line in separed:
        menu+="\n"

        caracteres = len(line)

        porcentaje = caracteres / size

        posicion = 0

        #Condicion que depende de los caracteres, se asigna una posicion.

        if porcentaje*100 >= 0 and porcentaje*100 <= 15:
            posicion = int(round(size*0.43))
        
        if porcentaje*100 > 15 and porcentaje*100 <= 40:
            posicion = int(round(size*0.34))
        
        if porcentaje*100 > 40 and porcentaje*100 <= 50:
            posicion = int(round(size*0.22))
        
        if porcentaje*100 > 50 and porcentaje*100 <= 65:
            posicion = int(round(size*0.18))

        if porcentaje*100 > 65 and porcentaje*100 <= 80:
            posicion = int(round(size*0.14))
        
        if porcentaje*100 > 80 and porcentaje*100 <= 100:
            posicion = int(round(size*0.03))

        #Total de caracteres
        total = (caracteres+1)/2

        #print (f"Caracteres: {len(line)}")
        #print (f"Caracteres + 1: {len(msj)+1}")
        #print (f"Total dividido: {total}")

        #Redondeo de total
        total = round(total)
        lado1 = int(round(size/2))
        lado2 = int(round(size/2))

        #print (f"Total redondeado: {total}")
        #print(f"Residuo: {len(msj) % 2}")

        #Condicion para que el menu se vea bien
        if not (caracteres - 2) % 4 == 0:
            lado2 -= 2

        #Condicion para que el menu se vea bien
        if caracteres % 2 == 1: 
            line += " "

        #print(f"Lado #1: {lado1-(total)}")
        #print (f"Caracteres en el msj: {total*2}")
        #print(f"Lado #2: {lado2-total}")

        #Calculo de la posicion del centro
        centro = lado1-posicion
        
        menu += f"{chars[1]}{chars[0]*((lado1)-centro)}{line}{chars[0]*((lado2-total*2)+centro)}{chars[2]}"

    #Footer del menu
    menu += f"\n{chars[3]}{chars[4]*(size-2)}{chars[3]}"

    return menu

startmenu = """Bienvenido al sistema de calificaciones de la institucion. Elija una opcion\n
(1) Verificar evaluacion\n
(2) Calcular promedio de notas\n
(3) Buscar calificaciones superiores\n
(4) Buscar calificaciones especificas\n
"""

user_in = "Usuario -> "

exit = False

calificaciones = input(f"{menu("Ingrese una o varias calificaciones separadas por comas\nSOLO son validas calificaciones entre 0 y 100")}\n{user_in}")

print(f"{menu(f"Calificaciones ingresadas: {calificaciones}")}")

calificaciones = calificaciones.split(',')

calificaciones = [int(x) for x in calificaciones]

calificaciones_validas = [x for x in calificaciones if 0 <= x <= 100]

input()

#Empieza el programa
while exit == False:
    try:
        option = int(input(f"{menu(startmenu)}\n{user_in}"))

        print(option)

        if option == 1:
            for index, calificacion in enumerate(calificaciones):
                if calificacion >= 60:
                    print(menu(f"El estudiante #{index+1} con la calificacion {calificacion} aprobó"))
                else:
                    print(menu(f"El estudiante #{index+1} con la calificacion {calificacion} reprobó"))
                
                input()

        elif option == 2:

            total = 0.0

            for num in calificaciones:
                total += num
            
            print(menu(f"Promedio de notas: {total/len(calificaciones)}"))

            input()

        elif option == 3:
            search = int(input(f"{menu("Ingrese un valor para comprobar cuantas calificaciones son mayores al valor")}\n{user_in}"))
            
            aproved = 0

            for calificacion in calificaciones_validas:
                if not calificacion > search:
                    continue
                aproved+=1
                
            print(menu(f"Calificaciones que superan el valor: {aproved}"))


            input() 

        elif option == 4:

            search = int(input(f"{menu("Ingrese un valor para comprobar cuantas calificaciones tienen ese valor")}\n{user_in}"))

            aproved = 0
            index = 0

            while index < len(calificaciones_validas):
                if calificaciones_validas[index] >= search:
                    aproved+=1
                index+=1

            print(menu(f"Calificaciones que superan el valor: {aproved}"))

            input()             

    except:
        try:
            if int(input(f"{menu(f"Ha ocurrido un error, ¿desea salir del programa?\n(1) Para salir. (2) Para quedarse.")}\n{user_in}")) == 1:
                exit == True
        except:
            print(menu("Ha digitado un valor incorrecto... El programa se cerrara automaticamente"))
            exit = True

print(menu("¡Muchas gracias por usar nuestro servicio!"))  

input()
    
clear()