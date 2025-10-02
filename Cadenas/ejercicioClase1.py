num1 = int(input("Número:"))
num2 = int(input("Número:"))

if num1 > num2:
    print("El mayor es", num1)
    for i in range(num2, num1 + 1):
        print(i)
elif num2 > num1:
    print("El mayor es", num2)
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("Son iguales")
    
media = (num1 + num2) / 2
print("La media es", media)

