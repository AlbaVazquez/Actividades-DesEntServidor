# Crear un programa que lea por teclado una cadena y un carácter, e inserte
# el carácter entre cada letra de la cadena. Ej: separar y , debería
# devolver s,e,p,a,r,a,r

cadena = input("Indica la cadena: ")
caracter = input("Indica el carácter: ")

print(caracter.join(cadena))



# Crear un programa que lea por teclado una cadena y un carácter, y
# reemplace todos los dígitos en la cadena por el carácter.
# Ej: su clave es: 1540 y X debería devolver su clave es: XXXX

cadena = input("Indica la cadena: ")
caracter = input("Indica el carácter: ")

for i in range(10):
    cadena=cadena.replace(str(i), caracter)

print(cadena)



# Crea un programa python que lea una cadena de caracteres y muestre la 
# siguiente información:

# -  La primera letra de cada palabra. Por ejemplo, si recibe Universal 
#     Serial Bus debe devolver USB.
# -   Dicha cadena con la primera letra de cada palabra en mayúsculas. 
#     Por ejemplo, si recibe república argentina debe devolver República 
#     Argentina.
# -   Las palabras que comiencen con la letra A. Por ejemplo, si recibe 
#     Antes de ayer debe devolver Antes ayer.

cadena = input("Indica una cadena: ")
lista = cadena.split(" ")
for palabra in lista:
    print(palabra[0], end="")
print()

for palabra in lista:
    print (palabra.capitalize(), end=" ")
print()

for palabra in lista:
    if palabra.startswith("a") or palabra.startswith("A"):
        print(palabra,end=",")
print()



# Escribir funciones que dadas dos cadenas de caracteres:

#  -  Indique si la segunda cadena es una subcadena de la primera.
#     Por ejemplo, cadena es una subcadena de subcadena.
#  -  Devuelva la que sea anterior en orden alfabético.
#     Por ejemplo, si recibe kde y gnome debe devolver gnome.

cadena1=input("Cadena 1:")
cadena2=input("Cadena 2:")	
if cadena1.find(cadena2)>-1:
	print ("cadena2 es subcadena de cadena1")
else:
	print ("cadena2 no es subcadena de cadena1")			

print(cadena1 if cadena1<cadena2 else cadena2)



# scribir un programa python que dado una palabra diga si es un palíndromo.
# Un palídromo Un palíndromo es una palabra, número o frase que se lee
# igual hacia adelante que hacia atrás. Ejemplo: reconocer

cadena=input("Cadena:")	
if cadena.lower()==cadena[::-1].lower():
		print("Es palindromo")
else:
		print("no es palindromo")