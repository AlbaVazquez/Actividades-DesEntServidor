class Persona():
    def __init__(self, nombre, apellidos, edad) -> None:
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellidos}, {self.edad}"


class Estudiante(Persona):
    def __init__(self, nombre, apellidos, edad):
        super().__init__(nombre, apellidos, edad)
        self.asignaturas = []
        
    def meterAsignatura(self, asignatura):
        if asignatura not in self.asignaturas:
            self.asignaturas.append(asignatura)
        else:
            print("El/La estudiante ya está matriculado/a en esa asignatura.")
            
    def quitarAsignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
        else:
            print("El/La estudiante no estaba matriculado/a en esa asignatura.")
            
    def mostrarAsignaturas(self) -> str:
        return [a.nombreA for a in self.asignaturas]
    
    def mostrarProfesores(self) -> list:
        profesores = []
        for a in self.asignaturas:
            if a.profesor.nombre not in profesores:
                profesores.append(a.profesor.nombre)
        return profesores


class Profesor(Persona):
    def __init__(self, nombre, apellidos, edad):
        super().__init__(nombre, apellidos, edad)
        self.imparte = []
    
    def meterImparte(self, asignatura):
        if asignatura not in self.imparte:
            self.imparte.append(asignatura)
        else:
            print("El/La profesor/a ya imparte esa asignatura.")
    
    def mostrarImparte(self):
        return [a.nombreA for a in self.imparte]


class Asignatura():
    def __init__(self, nombreA, horasS, profesor):
        self.nombreA = nombreA
        self.horasS = horasS
        self.profesor = profesor

        profesor.meterImparte(self)
        
    def __str__(self):
        return f"{self.nombreA}, {self.horasS}, {self.profesor}"        


class Grupo(Asignatura):
    def __init__(self, curso):
        self.curso = curso
        self.estudiantes = []
        
    def añadirAlumnos(self, alumno):
        if alumno not in self.estudiantes:
            self.estudiantes.append(alumno)
            
    def mostrarProfesores(self):
        profesoresRec = []
        for e in self.estudiantes:
            if e.mostrarProfesores() not in profesoresRec:
                profesoresRec.append(e.mostrarProfesores())
        return profesoresRec

#---------------------------------------------

raul = Persona('31', "Huertas", 28)
alicia = Estudiante("Alicia", "Maya", 28)
maria = Estudiante("María", "González", 29)
ignacio = Profesor("Ignacio", "Huertas", 40)
toni = Profesor("Toñi", "García", 40)
david = Profesor("David", "García", 40)

despliegue = Asignatura("Despliegue de aplicaciones web", 2, toni)
servidor = Asignatura("Desarrollo web en entorno servidor", 7, ignacio)
cliente = Asignatura("Desarrollo web en entorno cliente", 6, david)

daw2 = Grupo("2DAW")

#-----------------------------

daw2.añadirAlumnos(alicia)
daw2.añadirAlumnos(maria)

alicia.meterAsignatura(despliegue)
alicia.meterAsignatura(servidor)
alicia.meterAsignatura(cliente)
maria.meterAsignatura(cliente)

print("Asignaturas en las que está Alicia: ")
print(alicia.mostrarAsignaturas())

print("\nAsignaturas que imparte Ignacio: ")
print(ignacio.mostrarImparte())

alicia.quitarAsignatura(cliente)
print("\nAsignaturas de Alicia después de eliminar cliente: ")
print(alicia.mostrarAsignaturas())

print("\nProfesores de Alicia: ")
print(alicia.mostrarProfesores())

print("\nProfesores del curso 2DAW: ")
print(daw2.mostrarProfesores())
