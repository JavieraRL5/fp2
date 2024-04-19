def validarfolio():
    ticket_valido=False
    folio_valido=123
    print ("ingrese el numero de folio")
    n_folio=int(input())

    if n_folio==folio_valido:
        ticket_valido=True

        validafolio()


def suma(num1,nume2):
    resul=num1+nume2
    return resul
print("ingrese dos numeros")
num1= int(input())
num2=int (input())
print (suma(num1, num2))

