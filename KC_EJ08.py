
numero = int(input("Escribe un Numero:"))

if numero > 0 and (numero % 2) == 0:
  print ("el numero es Positivo y Par")
else:
  if numero  > 0 and (numero % 2) != 0:
    print ("el numero es Positivo e Impar")
  else:
   if numero  < 0 and (numero % 2) == 0:
    print ("el numero es Negativo y Par")
   else:
    if numero < 0 and (numero % 2) != 0:
     print ("el numero es Negativo e Impar")
    else:
      print ("No has escrito numero")

