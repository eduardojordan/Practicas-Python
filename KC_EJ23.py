
#clave = input("Escribe palabra -> terminar <- para finalizar!" )



while True:
  # = input ( " Escriba aca ´terminar´ si quiere detener el ciclo" )
  nombre= input("Introduzca Nombre:")
  notaUno= int(input("escriba Nota:"))
  notaDos= int(input("escriba Nota:"))
  notaTres= int(input("escriba Nota:"))
  calculo= (notaUno+notaDos+notaTres / 3)

  salida = input (" Escriba -terminar- si quiere detener, si no -enter- y continue" )
  if salida == "terminar":
    print ( nombre,"su promedio es" , calculo)
    break
  
   

 



