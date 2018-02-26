frase = input('Ingrese una frase:')
mi = frase.lower()
temp = mi.replace(' ','')

if temp == temp[::-1]: 
  print('La frase es palindromo') 
else: 
  print('No es palindromo')
  
  
  # Esta la consulte en internet y esta solucion funciona, pero no entiendo [::-1] , la funcion replace imagino quita los espacios, intente eliminar mi = frase.lower() y luego temp = replace(' ','') pero ya no funciona, si me puedes explicar un poco estas funciones