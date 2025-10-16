import pandas
from cargar_datos import cargarDatos

def mostrar_DataFrame(cargarDatos):
    lista_hamsters = []

    for indice, fila in cargarDatos.iterrows():
        lista_hamsters.append(fila.to_dict())

    dataFrame = pandas.DataFrame(lista_hamsters)
    return(dataFrame)

# print(\n{mostrar_DataFrame(cargarDatos)}')


#--------- FUNCIONES DE FILTRAR ---------------------------------------------------

def buscar_por_raza(cargarDatos, nombre) -> pandas.DataFrame:
    lista_resultados = []
    nombre_lower = nombre.lower()

    for indice, fila in cargarDatos.iterrows():
        raza_lower = fila['raza'].lower()
        if nombre_lower in raza_lower:
            lista_resultados.append(fila.to_dict())
    
    if not lista_resultados:
        resultado = print("No existe una raza que contenga esa palabra.")
        return resultado

    resultado = pandas.DataFrame(lista_resultados)
    return resultado

# nombre = 'winter'
# print(buscar_por_raza(cargarDatos, nombre))


def buscar_por_ev(cargarDatos, esperanzaVida) -> pandas.DataFrame:
    lista_resultados = []

    for indice, fila in cargarDatos.iterrows():
        filaEV = fila['esperanza_vida_anos']
        if filaEV >= esperanzaVida and filaEV < esperanzaVida+1:
            lista_resultados.append(fila.to_dict())
    
    if not lista_resultados:
        resultado = print("No existe una esperanza de vida aproximada para esa cifra.")
        return resultado
        
    resultado = pandas.DataFrame(lista_resultados)
    return resultado

# esperanzaVida = 2
# print(buscar_por_ev(cargarDatos, esperanzaVida))


def buscar_por_habitat(cargarDatos, habitatCm2):
    lista_resultados = []

    for indice, fila in cargarDatos.iterrows():
        filaHabitat = fila['habitat_min_cm2']
        if filaHabitat <= habitatCm2:
            lista_resultados.append(fila.to_dict())

    if not lista_resultados:
        resultado = print("Necesitas un hábitat más grande (mínimo 3000 cm2).")
        return resultado
        
    resultado = pandas.DataFrame(lista_resultados)
    return resultado
    
# habitatCm2 = 4500
# print(buscar_por_habitat(cargarDatos, habitatCm2))


def buscar_apto_principiantes(cargarDatos, apto):
    lista_resultados = []

    for indice, fila in cargarDatos.iterrows():
        filaApto = fila['apto_principiantes']
        if filaApto == apto:
            lista_resultados.append(fila.to_dict())
    
    resultado = pandas.DataFrame(lista_resultados)
    return resultado

# apto = True
# print(buscar_apto_principiantes(cargarDatos, apto))
    

def buscar_tipo_social(cargarDatos, tipoSocial):
    lista_resultados = []
    tipo_lower = tipoSocial.lower()

    for indice, fila in cargarDatos.iterrows():
        tipoSocial_lower = fila['tipo_social'].lower()
        if tipo_lower in tipoSocial_lower:
            lista_resultados.append(fila.to_dict())

    resultado = pandas.DataFrame(lista_resultados)
    return resultado
    
# tipoSocial = 'grupo'
# print(buscar_tipo_social(cargarDatos, tipoSocial))


#--------- FUNCIÓN PARA CALCULAR Y MOSTRAR ESTADÍSTICAS GENERALES ---------------------------------------------------

def calcular_eg(cargarDatos):
    promedio_ev = cargarDatos['esperanza_vida_anos'].mean()
    
    ev_max = cargarDatos['esperanza_vida_anos'].max()
    ev_min = cargarDatos['esperanza_vida_anos'].min()
    raza_ev_max = ''
    raza_ev_min = ''
    for indice, fila in cargarDatos.iterrows():
        if fila['esperanza_vida_anos'] == ev_max:
            raza_ev_max = fila['raza']
        
        if fila['esperanza_vida_anos'] == ev_min:
            raza_ev_min = fila['raza']
    
    promedio_tamano = cargarDatos['tamano_cm'].mean()

    tamano_max = cargarDatos['tamano_cm'].max()
    tamano_min = cargarDatos['tamano_cm'].min()
    raza_t_max = ''
    raza_t_min = ''
    for indice, fila in cargarDatos.iterrows():
        if fila['tamano_cm'] == tamano_max:
            raza_t_max = fila['raza']
        
        if fila['tamano_cm'] == tamano_min:
            raza_t_min = fila['raza']

    habitat_max_min = cargarDatos['habitat_min_cm2'].max()
    habitat_min_min = cargarDatos['habitat_min_cm2'].min()
    raza_h_max_min = ''
    raza_h_min_min = ''
    for indice, fila in cargarDatos.iterrows():
        if fila['habitat_min_cm2'] == habitat_max_min:
            raza_h_max_min = fila['raza']
        
        if fila['habitat_min_cm2'] == habitat_min_min:
            raza_h_min_min = fila['raza']

    aptos_principiantes = []
    no_aptos_principiantes = []
    for indice, fila in cargarDatos.iterrows():
        if fila['apto_principiantes']:
            aptos_principiantes.append(fila['raza'])
        else:
            no_aptos_principiantes.append(fila['raza'])

    resultado = ''
    resultado += f"Esperanza de vida promedio: {promedio_ev} años\n"
    resultado += f"Hámster más longevo: {raza_ev_max} -- Esperanza de vida: {ev_max} años\n"
    resultado += f"Hámster menos longevo: {raza_ev_min} -- Esperanza de vida: {ev_min} años\n\n"
    resultado += f"El tamaño promedio: {promedio_tamano} cm\n"
    resultado += f"Hámster más grande: {raza_t_max} -- Tamaño: {tamano_max} cm\n"
    resultado += f"Hámster más pequeño: {raza_t_min} -- Tamaño: {tamano_min} cm\n\n"
    resultado += f"Hámsters aptos para principiantes: {aptos_principiantes}\n"
    resultado += f"Hámsters no aptos para principiantes: {no_aptos_principiantes}\n\n"
    resultado += f"Hámster que más territorio necesita: {raza_h_max_min} -- Hábitat mínima (cm2): {habitat_max_min}\n"
    resultado += f"Hámster que menos territorio necesita: {raza_h_min_min} -- Hábitat mínima (cm2): {habitat_min_min}\n"
    return resultado

# print(calcular_eg(cargarDatos))

#--------- FUNCIÓN PARA BUSCAR POR DESCRIPCIÓN ---------------------------------------------------

def buscar_temperamento(cargarDatos, palabra):
    lista_resultados = []
    palabra_lower = palabra.lower()

    for indice, fila in cargarDatos.iterrows():
        temperamento_lower = fila['temperamento'].lower()
        if palabra_lower in temperamento_lower:
            resultado = {
                'raza': fila['raza'],
                'temperamento': fila['temperamento']
            }
            lista_resultados.append(resultado)
            
    return pandas.DataFrame(lista_resultados).to_string() #Esta vez lo paso a string para que me muestre el campo de temperamento completo
        
# palabra = "Dócil"
# print(buscar_temperamento(cargarDatos,palabra))