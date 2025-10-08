# -----------------------------
# Gestión de Biblioteca Digital
# -----------------------------

# Funciones
import json

def mostrar_libros(biblioteca):
    # Recorre la lista y muestra la información de cada libro
    for libro in biblioteca:
        print(f"Título: {libro["titulo"]} - Autor: {libro["autor"]} \nAño: {libro["anio"]} - Género: {libro["genero"]} \n --------")
    pass


def buscar_por_autor(biblioteca, autor):
    # Devuelve una lista con los títulos de un autor dado
    listaLibros = []
    print("Libros del autor ", autor, ": ")
    for libro in biblioteca:
        if libro["autor"].lower() == autor.lower():
           listaLibros.append({libro["titulo"]})
    print(listaLibros)
    pass


def prestamo(biblioteca, titulo, usuario):
    # Registra un préstamo de un libro por un usuario
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            if usuario in libro["prestamos"]:
                libro["prestamos"][usuario] += 1
            else:
                libro["prestamos"][usuario] = 1
            print (f"Préstamo del libro {titulo} registrado para el usuario {usuario}")
    pass


def libro_mas_popular(biblioteca):
    # Devuelve el libro con más préstamos totales
    masPrestamos = 0
    masPopular = ""
    
    for libro in biblioteca:
        totalPrestamos = sum(libro["prestamos"].values())
        if totalPrestamos > masPrestamos:
            masPrestamos = totalPrestamos
            masPopular = libro["titulo"]
    print("El libro más popular es ", masPopular)
    pass


def estadisticas_usuarios(biblioteca):
    estadisticas = {}
    for libro in biblioteca:
        for usuario, cantidad in libro["prestamos"].items():
            if usuario in estadisticas:
                estadisticas[usuario] += cantidad
            else:
                estadisticas[usuario] = cantidad
    return estadisticas

def guardar_biblioteca(biblioteca, nombre_fichero):
    # Guarda la biblioteca en un fichero JSON
    
    with open(nombre_fichero, 'w') as fichero:
        json.dump(biblioteca, fichero)
    pass

def cargar_biblioteca(nombre_fichero):
    # Carga la biblioteca desde un fichero JSON
    with open(nombre_fichero, 'r') as fichero:
        biblioteca = json.load(fichero)
    return biblioteca
    
def exportar_resumen(biblioteca, nombre_fichero):
    # Exporta un resumen de la biblioteca a un fichero de texto
    with open(nombre_fichero, 'w') as fichero:
        for libro in biblioteca:
            totalPrestamos = sum(libro["prestamos"].values())
            fichero.write(f"Título: {libro['titulo']}  |  Autor: {libro['autor']}  |  Préstamos: {totalPrestamos}\n")
    pass


# Programa principal
def main():
    # 1. Crear biblioteca con al menos 5 libros
    biblioteca = [
        {
            "titulo": "Cien años de soledad",
            "autor": "Gabriel García Márquez",
            "anio": 1967,
            "genero": "Novela",
            "prestamos": {}
        },
        {
            "titulo": "El Quijote",
            "autor": "Miguel de Cervantes",
            "anio": 1605,
            "genero": "Novela",
            "prestamos": {}
        },
        {
            "titulo": "El diario de Anne Frank",
            "autor": "Anne Frank",
            "anio": 1942,
            "genero": "Diario",
            "prestamos": {}
        },
        {
            "titulo": "El libro más malo del mundo",
            "autor": "Amador Rivas",
            "anio": 2003,
            "genero": "Humor",
            "prestamos": {}
        },
        {
            "titulo": "Un libro genérico",
            "autor": "Alguien",
            "anio": 2024,
            "genero": "Humor",
            "prestamos": {}
        }
        # Añadir más libros aquí...
    ]

    # 2. Mostrar todos los libros
    print("\n--- ACTIVIDAD 2 ---")
    mostrar_libros(biblioteca)
    # 3. Buscar por autor (pedir al usuario un nombre)
    print("\n---- ACTIVIDAD 3 ---")
    autor = input("Autor a buscar: ")
    buscar_por_autor(biblioteca, autor)
    # 4. Simular préstamos
    print("\n---- ACTIVIDAD 4 ---")
    titulo = input("Título del libro a prestar: ")
    usuario = input("Nombre de usuario : ")
    prestamo(biblioteca, titulo, usuario)
    # 5. Mostrar el libro más popular
    print("\n---- ACTIVIDAD 5 ---")
    libro_mas_popular(biblioteca)
     # 6. Mostrar estadísticas de usuarios
    print("\n---- ACTIVIDAD 6 ---")
    print("\n Estadísticas de préstamos:")
    estadisticas = estadisticas_usuarios(biblioteca)
    for usuario, total in estadisticas.items():
        print(f"  - {usuario}: {total}")
    # 7. Guardar biblioteca en fichero JSON
    print("\n---- ACTIVIDAD 7 ---")
    guardar_biblioteca(biblioteca, "biblioteca.json")
    print("Biblioteca guardada en 'biblioteca.json'")
    # 8. Cargar biblioteca desde fichero JSON
    print("\n---- ACTIVIDAD 8 ---")
    biblioteca_cargada = cargar_biblioteca("biblioteca.json")
    print(biblioteca_cargada)
    # 9. Exportar resumen a fichero de texto
    print("\n---- ACTIVIDAD 9 ---")
    exportar_resumen(biblioteca, "resumen_biblioteca.txt")
    print("Resumen exportado a 'resumen_biblioteca.txt'")


# Ejecutar programa
if __name__ == "__main__":
    main()