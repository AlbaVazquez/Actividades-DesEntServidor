#Crear una función que utilice args, y otra con kwargs

def funcion_args(n,*args):
    # resultado = n
    # for arg in args:
    #     resultado += arg
    # return resultado
    
    mayorN = n
    for arg in args:
        if (arg > mayorN):
            mayorN = arg
            
    resultado = print("El parámetro más grande es", mayorN)
    return resultado
        
def funcion_kwargs(nombre = "alba", **kwargs):
    persona = [nombre]
    for key, value in kwargs.items():
        persona.append(f"{key}: {value}")
    return persona
        
#Llamada a las funciones
print(funcion_args(1, 7, 3))

print("-----")

print(funcion_kwargs(edad=19, ciudad="Dos Hermanas"))