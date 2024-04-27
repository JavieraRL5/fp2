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