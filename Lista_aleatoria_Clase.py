import random

lista_alumnos = [
    "Cardoso Munoz, Jesus Manuel",
    "Carvajal Sánchez, Irene",
    "Díaz Alfaro, Carmen",
    "Fernández Aido, David",
    "Gallo Muñoz, Ismael",
    "Gómez Jiménez, Iván",
    "Jiménez López, Miguel",
    "López Rufino, Rubén",
    "Luna Del Valle, Jaime",
    "Maya Ureba, Alejandro",
    "Moreno Valcárcel, Leandro Abdiel",
    "Norte Díaz, Carlos",
    "Ojeda Balsera, Daniel",
    "Palma Méndez, Raimundo",
    "Paz Fernández, Pablo",
    "Pulido Carmona, Miguel",
    "Romero Haro, Andrea",
    "Rubio Casado, Jaime",
    "Ruiz Lerma, Marcos",
    "Sánchez Paniagua, Blas",
    "Vázquez Guillén, Alba"
]

lista_alumnos_No = lista_alumnos.copy() #Los alumnos que no han salido
lista_alumnos_Si = []   #Los alumnos que sí han salido




#------ INTERFAZ -------------------------

while True:
    print("\n", "="*20)
    print("1. Generar un alumno")
    print("2. Ver los alumnos que no han salido")
    print("3. Ver los alumnos que sí han salido")
    print("4. Salir")
    print("="*20)
    
    try:
        opcion = int(input("Selecciona una valor(1-4): "))
    except ValueError:
        print("Introduce un valor válido")
    print("\n")
    
    if opcion == 4:
        break
    
    elif opcion == 1:
        if lista_alumnos_No:
            alumno_seleccionado = random.choice(lista_alumnos_No)
            lista_alumnos_Si.append(alumno_seleccionado)
            lista_alumnos_No.remove(alumno_seleccionado)
            print(f"\nLe toca a: {alumno_seleccionado}")
            print("-"*20)
        else:
            print("\nTODOS HAN SALIDO, LA LISTA SE HA REINICIADO")
            lista_alumnos_No = lista_alumnos.copy()
            lista_alumnos_Si = []
            
    elif opcion == 2:
        if lista_alumnos_No:
            for nombre in lista_alumnos_No:
                print(nombre)
        else:
            print("\nNO QUEDAN ALUMNOS POR SALIR\n")
    
    elif opcion == 3:
        if lista_alumnos_Si:
            for nombre in lista_alumnos_Si:
                print(nombre)
        else:
            print("\nNO HA SALIDO NADIE AÚN\n")