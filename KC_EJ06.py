numberOne = input ("Escribe el primer numero")
numberTwo = input ("escribe el segundo numero")

numberOne = int(numberOne)
numberTwo = int(numberTwo)


if numberOne < numberTwo:
 #print ("El primer numero es menor que el primero = False" )
  print (numberOne,"<", numberTwo, "= False" )
elif numberOne > numberTwo:
  print (numberOne,">", numberTwo,"= True")
elif numberOne == numberTwo:
  print (numberOne,"y", numberTwo, "Son iguales = False")
elif numberOne != numberTwo:
  print (numberOne,"y", numberTwo, "Son distintos = True")
