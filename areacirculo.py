def calculaAreaCirc(num): 
        area=(num*num)*3.14
        return area 

print ("ingrese en numero")
num=int (input())
print (calculaAreaCirc(num))


# def define nombre de una funcion  (calculaAreaCirc)
# "num" puede ir textual el argumento o de una vez el numero
#  se ingresa la funcion y se multiplica por si mismo 
# Funcion: calculaAreaCirc
# variable:  area=(num*num)*3.14


def area_circulo():
        print ("ingrese el radio")
        radio=int(input())
        pi=3.14
        area=pi*(radio**2) 

        print ("el area del circulo es", area)
        # return area

        area_circulo()