ticket_valido=False
folio_valido=123
print ("ingrese el numero de folio")
num_folio=int(input())

if num_folio==folio_valido:
    ticket_valido=True

if ticket_valido:
        print("ticket valido")

else:
      print ("este ticket caducó")        
