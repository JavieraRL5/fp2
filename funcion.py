def multi (num1, num2):
    result=num1*num2
    return result

def resta (num1, num2):
    result=num1-num2
    return result

def suma (num1, num2):
    result=num1+num2
    return result

def divi (num1,num2):
    result= num1/num2
    return result




print ("Seleccione una opcion")
print ("1.- - Suma")
print ("2.- -Resta")
print ("3.- -Multiplicación")
print ("4.-  -División")
op=int (input())
match op:
    case 1:
        num1=int(input ("ingresa un numero"))
        num2=int(input ("Ingresa el segundo numero"))
        print(suma (num1, num2))
    case 2:
        num1=int(input ("ingresa un numero"))
        num2=int(input ("Ingresa el segundo numero"))
        print (resta (num1,num2))
    case 3:
        num1=int(input ("ingresa un numero"))
        num2=int(input ("Ingresa el segundo numero"))
        print (multi(num1,num2))
    case 4:
        num1=int(input ("ingresa un numero"))
        num2=int(input ("Ingresa el segundo numero"))          
        print (divi(num1,num2))
