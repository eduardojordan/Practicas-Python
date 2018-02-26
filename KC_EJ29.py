
def promedio (notaUno = 0 ,notaDos = 0,notaTres = 0):
 
  promedio = ((notaUno + notaDos + notaTres) / 3)
  
  #print (promedio)
  

diccionario = {}
while True:
  nombre = input("Introduzca Nombre:")
  notaUno = int(input("escriba Nota:"))
  notaDos = int(input("escriba Nota:"))
  notaTres = int(input("escriba Nota:"))
  promedio (notaUno,notaDos,notaTres)
  diccionario[nombre]=promedio
 
 
  orden = [(k,v) for v,k in sorted ([(v,k) for k,v in diccionario.items()],reverse = True)]
  salida = input (" Escriba -terminar- si quiere detener, si no -enter- y continue" )
  if salida == "terminar":
     print (diccionario)
     break
   
   
   # Al final sale este error, entiendo que es de memoria o por el hecho de que los numeros sea decimales ---->>> {'Pedro': <function promedio at 0x7ff53bfefe18>, 'Joe': <function promedio at 0x7ff53bfefe18>}
   