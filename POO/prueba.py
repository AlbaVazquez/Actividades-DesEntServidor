class Pelicula():
    
    def __init__(self, titulo, director, anio) -> None:
        self.titulo = titulo
        self.director = director
        self.anio = anio
        
    def __str__(self):
        return f"{self.titulo}, {self.anio} - {self.director}"
        
pelicula1 = Pelicula("pelicula1", "yo", 2025)
pelicula2 = Pelicula("pelicula2", "alguien", 2026)
pelicula3 = Pelicula("pelicula3", "otro", 2025)
print(f"{pelicula1.titulo} del director {pelicula1.director} del año {pelicula1.anio}")

class BibliotecaPeliculas():
    def __init__(self) -> None:
        self.lista = []
        
    def anadirPelicula(self, Pelicula):
        self.lista.append(Pelicula)
        
    def __str__(self) -> str:
        peliculaStr = ""
        for i in self.lista:
            peliculaStr += f"- {i}\n"
        return peliculaStr
    
    def FiltrarAnio(self, anio):
        encontradas = ""
        for i in self.lista:
            if i.anio == anio:
                encontradas += f"~ {i}\n"  
        return encontradas

lista1 = BibliotecaPeliculas()
lista2 = BibliotecaPeliculas()

lista1.anadirPelicula(pelicula1)
lista1.anadirPelicula(pelicula2)
lista2.anadirPelicula(pelicula3)

print(lista1)

print(lista1.FiltrarAnio(2026))