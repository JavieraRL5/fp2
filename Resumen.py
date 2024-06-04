# Entrada y Salida 
# Print ("ingresa un nombre:  ")
# nombre_usuario = input ()
# print ("ingresa un apellido: ")
# apellido=input ()
# print ("hola, " + nombre_usuario + " "apellido" +"! este es tu primer programa.")


# print ("por favor ingresa un numero")
# num = int (input())
# print ("por favor, ingresa otro numero")
# num2= int (input ())
# print ("ingresa un numero")
# num3= int (input ())

# if num>num2 and num>num3:
#     print ("el  " + str (num) +  " es mayor ") 
# elif num2>num3:
#     print ("el "+ str (num2) + "es mayor que")
# else:
#     print ("el  " + str (num3) + "es mayor ")


#  Validar si un ticket esta dentro del rango valido entre 100 y 750

print ("Ingrese el numero de Ticket")
num_ticket = int (input()) 

if num_ticket >= 100 and num_ticket <=750:

    if num_ticket >= 100 and num_ticket <=500: 
        print ("Entrada valida! Ingreso Cancha")
    if num_ticket >500 and num_ticket <=750:
        print ("Entrada valida! Acceso Cancha")
else:
    print("ACCESO DENGADO")    