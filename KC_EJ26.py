veces= int(input("cuantas veces:"))

def imprimir (texto, veces = 1):
 print("<table>")
 print (texto * veces)
 print("<table>")
  


imprimir("<tr><td></td></tr> \n",veces)