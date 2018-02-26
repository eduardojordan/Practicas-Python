numberOne = input ("Escribe un numero")
numberTwo = input ("escribe otro numero")
numberThree = input ("escribe un ultimo numero")

numberOne = int(numberOne)
numberTwo = int(numberTwo)
numberThree = int(numberThree)



if (numberOne > numberTwo) and (numberOne > numberThree) :
  print (numberOne, "es el de mayor valor")
elif (numberTwo > numberOne) and (numberTwo > numberThree):
  print (numberTwo,"es el de mayor valor")
elif (numberThree > numberOne) and (numberThree > numberTwo):
  print (numberThree, "es el de mayor valor")
  
if (numberOne < numberTwo) and (numberOne < numberThree) :
  print (numberOne, "es el de menor valor")
elif (numberTwo < numberOne) and (numberTwo < numberThree):
  print (numberTwo,"es el de menor valor")
elif (numberThree < numberOne) and (numberThree < numberTwo):
  print (numberThree, "es el de menor valor")



