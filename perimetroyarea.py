def perimetro (a,b):  #definicion de argumentos 
    resul=a*2+b*2  #funcion 
    return resul
def area (a,b):  #definición de aregumentos 
    resul=a*b 
    return resul
print ("ingrese lado A y b ")
a=int(input())
b=int (input())
print (perimetro (a,b))
print (area(a,b))
