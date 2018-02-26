from random import randint

aleatorio = (randint(1, 100))
print("Debes Adivininar un numero entre 1 y 100 , solo tienes -> 5 INTENTOS")

oportunidades = 0


while oportunidades < 5:
    tuNumero = int(input('Introduce un número del 1 al 100:'))
    oportunidades = oportunidades +1
    if tuNumero < aleatorio:
      print('Intenta con un numero Mayor, intentos',oportunidades)
    if tuNumero > aleatorio:
      print('Intenta con un numero Menor')
    if tuNumero == aleatorio:
      print('Has Ganado!!! :)')
      break
    if oportunidades == 5:
      print( "Se han agotado las oportunidades :( , el numero era:",aleatorio)


  
   

 



