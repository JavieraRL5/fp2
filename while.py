def primerwhile():
 text=""

 while text !="hi":
    print("Ingrese el saludo correcto")
    text=input()
 print("Ese es el saludo correcto")

# primerwhile()

def verifpassw():
 passw=""
 print("Ingrese su password ")
 passw=input()
 while passw !="1234" and cont <3:
    print("Su password es incorrecta")
    cont=cont+1
    passw=input()
    if cont ==3:
        print (" Usted ha bloqueado la contraseña")
print("Bienvenido Usuario Admin")

verifpassw()

#ComeLaCena

def ComeCena():
  cantComida=100

  while cantComida !=0:
    print ("Desea Comer?")
    cucharada=input()
    if cucharada== "si":
      cantComida= cantComida-25
      print ("la cantidad de comida es " , cantComida)
    else:
      print("Usted ya no quiere comida")
      cantComida=0

      ComeCena()


def cantMicros():
  cantMicros=0
  #Las micros pasan solo hasta las 12
  #El usuario comienza a esperar a las 8 
  #Cada vez que dice que no,pasa una hora 
  while cantMicros !=int(3) and hora !=  (12):

    print("ha pasado una micro?")
    resp=input()

    if resp ==("si"):
      cantMicros=cantMicros+int1
      print("La cantidad de micros que han pasado") 
      if cantMicros == int (3):
        print ("\nse acabaron las micros")
    if resp ==("no"):
      hora=hora+int(1) 