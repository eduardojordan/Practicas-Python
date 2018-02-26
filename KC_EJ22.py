
electores =  {}


for veces in range (3):
  nombre=input('Introduce el nombre del participante:')
  edad=int(input('Introduce su edad:'))
  if edad > 18:
   electores[nombre] = edad



print ("Tienes derecho a voto:", list(electores.keys()))

