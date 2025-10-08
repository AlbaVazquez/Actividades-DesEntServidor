#Crear una función que utilice args, y otra con kwargs

def funcion_args(*args):
    for arg in args:
        print(arg)
        
def funcion_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
#Llamada a las funciones
funcion_args(1, 2, 3, 'cuatro', 'cinco')
print("-----")
funcion_kwargs(nombre="Juan", edad=30, ciudad="Madrid")