diccionario= {}
while True:

  nombre = input("Introduzca Nombre:")
  notaUno = int(input("escriba Nota:"))
  notaDos = int(input("escriba Nota:"))
  notaTres = int(input("escriba Nota:"))
  calculo = ((notaUno + notaDos + notaTres) / 3)
  diccionario[nombre]=calculo
  #Para presentar en orden descendiente por valor 
  orden= [(k,v) for v,k in sorted ([(v,k) for k,v in diccionario.items()],reverse = True)]
  
  salida = input (" Escriba -terminar- si quiere detener, si no -enter- y continue" )
  if salida == "terminar":
    print (orden)
    break
    
 
  
   

 



