numberOne = input ("Escribe una nota")
numberTwo = input ("escribe segunda nota")
numberThree = input ("escribe tercera nota")

numberOne = int(numberOne)
numberTwo = int(numberTwo)
numberThree = int(numberThree)

suma = (numberOne + numberTwo + numberThree)

calcula = (suma / 3)

if calcula < 4:
 print ("No Apto" )
elif calcula > 4:
  print ("Apto")
