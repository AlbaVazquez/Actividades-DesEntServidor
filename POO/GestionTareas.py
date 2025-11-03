import json

class Tarea():
    def __init__(self, titulo, descripcion, prioridad, fecha_vencimiento, completada):
        self.titulo = titulo;
        self.descripcion = descripcion;
        self.prioridad = prioridad;
        self.fecha_vencimiento = fecha_vencimiento;
        self.completada = completada;
        
    def __str__(self):
        return f"{self.titulo}, {self.descripcion}, {self.prioridad}, {self.fecha_vencimiento}, {self.completada}"
    
    def marcar_completada(self):
        self.completada = True
    
    def actualizar(self):
        while True:
            print ("-" * 20, "\n¿Qué quieres actualizar")
            print ("1. Titulo \n2. Descripción \n3. Prioridad \n4. Fecha de vencimiento \n5. Salir", "-" * 20, "\n")
            opcion = input ("Selecciona una opción (1-5): \n")
            
            if opcion == "1":
                campo = input("Nuevo título: ")
                self.titulo = campo
            
            elif opcion == "2":
                campo = input("Nueva descripción: ")
                self.descripcion = campo
                
            elif opcion == "3":
                campo = input("Nueva prioridad: ")
                self.prioridad = campo
                
            elif opcion == "4":
                campo = input("Nueva fecha de vencimiento: ")
                self.fecha_vencimiento = campo
            
            elif opcion == "5":
                break
            
            else:
                print("Elige una opción válida.")
    
    def mostrar_informacion(self):
        print(self)
    
    
class GestorTareas():
    def __init__(self):
        self.listaTareas = []
        
    def __str__(self):
        return f"{self.listaTareas}"
    
    def agregar_tarea(self, Tarea):
        if Tarea not in self.listaTareas:
            self.listaTareas.append(Tarea)
    
    def eliminar_tarea(self, Tarea):
        if Tarea in self.listaTareas:
            self.listaTareas.remove(Tarea)
    
    def actualizar_tarea(self, Tarea):
        if Tarea in self.listaTareas:
            Tarea.actualizar()
    
    def listar_tareas(self):
        prioridad_orden = {"Alta":1, "Media":2, "Baja":3}
        lista_ordenada = sorted(self.listaTareas, key=lambda t: prioridad_orden[t.prioridad])
        
        print("--- TAREAS PENDIENTES ---")
        for tarea in lista_ordenada:
            if not tarea.completada:
                print(f"- {tarea.titulo} ({tarea.prioridad})")
        
        print("--- TAREAS COMPLETADAS ---") 
        for tarea in lista_ordenada:
            if tarea.completada:
                print(f"- {tarea.titulo} ({tarea.prioridad})")
    
    def guardar_tareas(self, archivo="tareas.json"):
        datos = []
        
        for t in self.listaTareas:
            datos.append({
                "titulo": t.titulo,
                "descripcion": t.descripcion,
                "prioridad": t.prioridad,
                "fecha_vencimiento": t.fecha_vencimiento,
                "completada": t.completada
            })
            
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        
    
    def cargar_tareas(self, archivo = "tareas.json"):
        self.listaTareas = []
        
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                
            for d in datos:
                tarea = Tarea(d["titulo"], d["descripcion"], d["prioridad"], d["fecha_vencimiento"], d["completada"])
                self.listaTareas.append(tarea)
                
        except FileNotFoundError:
            self.listaTareas = []
        
        return self.listaTareas
    
# CREACIÓN DE OBJETOS ---------------------
gestor1 = GestorTareas()
tareas = gestor1.cargar_tareas()

tarea1 = Tarea("Actividad 1", "actividad de Despliegue de APWeb", "Baja", "16-11-2025", False)
tarea2 = Tarea("Actividad 2", "actividad de DesEntCLiente", "Media", "30-11-2025", False)
tarea3 = Tarea("Actividad 3", "actividad de DesEntServidor", "Alta", "4-11-2025", False)

gestor1.agregar_tarea(tarea1)
gestor1.agregar_tarea(tarea2)
gestor1.agregar_tarea(tarea3)

gestor1.guardar_tareas()

gestor1.listar_tareas()
