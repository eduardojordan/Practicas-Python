
cuenta=0
numerosPares = []

for cuenta in range (10):
  numero = int(input ("Introduce un numero "))
  if (numero % 2) == 0 :
    numerosPares.append(numero)
    cuenta = cuenta +1
  if cuenta == 10:
    print (numerosPares)


 
