numberOne = input ("Escribe una cantidad")
numberOne = int(numberOne)

EurtoDollar  = (numberOne * 1.06 )
DollartoEur  = (numberOne / 1.06 )

  #print ("Selecciona una Opcion")
 # print ("Euro to Dollar - Opcion 1")
 # print ("Dollar to Euro - Opcion 2")
  
opcion = input ("Selecciona (1) de Euros a Dollar y (2) de Dollar a Euros")
opcion = int(opcion)
  
if opcion == 1:
  print (EurtoDollar, "USD")
elif opcion == 2:
  print (DollartoEur, "Euros")
