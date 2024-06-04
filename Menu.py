# "_" guión bajo sirve para cualquier numero que tu no definas.
# Para salir cambio el "Stay" de TRUE a FALSE

stay= True 
while stay:
 print ("Bienvenido al sistema Python--")
 print ("Seleccione una opcion")
 print ("1.- Escriba su nombre")
 print ("2.- ingrese gasté")
 print ("3.- ingrese su año de nacimiento")
 print ("3.- mis gastos")
 print ("4.- Salir")

 opcion=int (input ())
 
 match opcion:
     case 1: 
         nombre=input()
     case 2:
         gasto=gasto + int (input())
     case 3:
         print("Hola", nombre, "y su edad es", "usted ha gastado", gasto)
     case 4:
         Stay=False
     case _:  
         print ("menú inválido")
    