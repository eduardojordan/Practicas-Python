entrada = input ("Escribe una consonante o vocal en minuscula, que yo te digo que es:")

#Creo una tupla
vocales = ("a","e","i","o","u")

#Nota personal para referenciar la tupla se usa "in"

if entrada in vocales:
  print ( entrada, "Es una vocal")
else:
  print (entrada, "es una consonante")



