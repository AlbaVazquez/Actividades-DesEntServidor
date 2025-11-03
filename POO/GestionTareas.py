class Tarea():
    def __init__(self, titulo, descripcion, prioridad, fecha_vencimiento, completada):
        self.titulo = titulo;
        self.descripcion = descripcion;
        self.prioridad = prioridad;
        self.fecha_vencimiento = fecha_vencimiento;
        self.completada = completada;
        
    def __str__(self):
        return f"{self.titulo}, {self.descripcion}, {self.prioridad}, {self.fecha_vencimiento}, {self.completada}"
    
    def marcar_completada():
        pass
    
    def actualizar():
        pass
    
    def mostrar_informacion():
        pass
    
    
class GestorTareas():
    def __init__(self):
        listaTareas = []
        
    def __str__(self):
        return f"{self.listaTareas}"
    
    def agregar_tarea():
        pass
    
    def aliminar_tarea():
        pass
    
    def actualizar_tarea():
        pass
    
    def listar_tareas():
        pass
    
    def guardar_tareas():
        pass
    
    def cargar_tareas():
        pass