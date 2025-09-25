lista=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]	

cadena=input("Cadena:")
if cadena in lista:
	print("La cadena está en la lista")
else:
	print("La cadena no está en la lista")	

print(lista.count(cadena))	

cadena2=input("Cadena a reemplazar:")
apariciones=lista.count(cadena)
pos=0
for i in range(0,apariciones):
    # buscará la posición dentro de la lista que contenga la cadena a encontrar
	pos=lista.index(cadena,pos)
	lista[pos]=cadena2
print(lista)