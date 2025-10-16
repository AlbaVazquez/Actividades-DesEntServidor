import requests #Librería para hacer solicitudes HTTP
import pandas #Librería para manipulación de datos
import json

json_url = "https://raw.githubusercontent.com/AlbaVazquez/Ejercicios-AlbaVazquezGuillen/main/hamsters.json"

def cargar_datos_hamsters():
    
    print("\nIntentando cargar datos de hamsters...")
   
    try:
        respuesta = requests.get(json_url)
        respuesta.raise_for_status() #Excepción si existe algún error
    
        datos_json = respuesta.json() #Converción a una lista de diccionarios
    
        df_hamsters = pandas.DataFrame(datos_json) #Almacenamiento en DataFrame
        return df_hamsters
    
    #Para considerar los posibles errores le he pedido a la ia que me diga cuáles podrían surgir
    except requests.exceptions.RequestException as e:
        print(f"ERROR: falló la conexión o la descarga. Asegúrate de tener conexión. \nDetalle del error: {e}")
        return None

    except json.JSONDecodeError:
        print(f"ERROR: el archivo descargado no es un Json válido o está vacío.")
        return None
    
    
#PARA PROBAR EL MÓDULO:
    
    #python3 -m venv env
    #source env/bin/activate
    ##pip install pandas && pip install requests
    
    #pip install -r requirements.txt
    
cargarDatos = cargar_datos_hamsters()
if cargarDatos is not None:
    print("\n✅ ✅ ✅......... DATOS CARGADOS CORRECTAMENTE .........✅ ✅ ✅")
    # print(cargarDatos)

