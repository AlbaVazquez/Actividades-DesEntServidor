import procesar_datos
from cargar_datos import cargarDatos
import pandas

def mostrar_menu_principal():
    print("\n" + "="*40)
    print("        MENÚ PRINCIPAL GUÍA HÁMSTERS")
    print("="*40)
    print("1. Mostrar todos los datos")
    print("2. Filtrar Datos (Búsqueda específica)")
    print("3. Resumen de Estadísticas Generales")
    print("4. Buscar por temperamento")
    print("5. Salir")
    print("-" * 40)
# print(mostrar_menu_principal())

def mostrar_menu_filtrado():
    print("\n" + "~"*30)
    print("     MENÚ DE FILTRADO")
    print("~"*30)
    print("1. Por Raza")
    print("2. Por Esperanza de Vida")
    print("3. Por Tamaño de Hábitat")
    print("4. Por Aptitud para Principiantes")
    print("5. Por Tipo Social")
    print("6. Volver al Menú Principal")
    print("-" * 30)
# print(mostrar_menu_filtrado())

def mostrar_menu_temperamento():
    print("1.Solitario      5.Dócil")
    print("2.Territorial    6.Rápido")
    print("3.Tranquilo      7.Tímido")
    print("4.Activo         8.Propenso a morder\n")
    print("9.Volver al Menú Principal")
# print(mostrar_menu_temperamento())

while True:
    mostrar_menu_principal()
    opcion = input("Elige una opción (1-5): ")

    # OPCION 1: mostrar todos los datos --------
    if opcion == '1':
        print("\n" + "-"*50 + " TABLA COMPLETA DE HAMSTERS " + "-"*50)
        df_completo = procesar_datos.mostrar_DataFrame(cargarDatos)
        print(df_completo)
        print("-"*130)
    
    # OPCION 3: mostrar resumen de estadísticas generales --------
    elif opcion == '3':
        print("\n" + "-"*30 + " RESUMEN DE ESTADÍSICAS GENERALES " + "-"*30)
        resumen = procesar_datos.calcular_eg(cargarDatos)
        print(resumen)
        print("-"*95)
    
    # OPCION 5: salir --------
    elif opcion == '5':
        break

    # OPCION 2: filtrar campos --------
    elif opcion == '2':
        while True:
            mostrar_menu_filtrado()
            sub_opcion = input("Elige un filtro (1-6): ")

            # SUB-OPCIÓN 1: filtrar por raza
            if sub_opcion == '1':
                parametro = input("Introduce una raza: ")
                resultado_df = procesar_datos.buscar_por_raza(cargarDatos, parametro)
                print(resultado_df)

            # SUB_OPCION 2: filtrar por esperanza de vida
            elif sub_opcion == '2':
                try:
                    parametro = float(input("Introduce una esperanza de vida en años (1-3): "))
                    resultado_df = procesar_datos.buscar_por_ev(cargarDatos, parametro)
                    print(resultado_df)
                except ValueError:
                    print("Introduce una opción válida")

            # SUB-OPCIÓN 3: filtrar por tamaño de hábitat 
            elif sub_opcion == '3':
                try:
                    parametro = float(input("Introduce un mínimo en cm2 para un hábitat (3000-4500): "))
                    resultado_df = procesar_datos.buscar_por_habitat(cargarDatos, parametro)
                    print(resultado_df)
                except ValueError:
                    print("Introduce una opción válida")

            # SUB-OPCIÓN 4: filtrar por acto para principiantes 
            elif sub_opcion == '4':
                apto = input("Apto para principiantes (S/s), No apto para principiantes (N/n): ")
                
                if apto.lower() == "s":
                    parametro = True
                else:
                    parametro = False

                resultado_df = procesar_datos.buscar_apto_principiantes(cargarDatos, parametro)
                print(resultado_df)

            # SUB-OPCIÓN 5: filtrar por tipo social
            elif sub_opcion == '5':
                grupoSocial = input("Indica un tipo social. Solitario (1), Pareja (2), Grupo (3): ")
                parametro = ''

                if grupoSocial == "1":
                    parametro = "Solitario"
                    
                elif grupoSocial == "2":
                    parametro = "Pareja"

                elif grupoSocial == "3":
                    parametro = "Grupo"
                    
                else:
                    print("Introduce una opción válida.")
                
                if parametro:
                    print(procesar_datos.buscar_tipo_social(cargarDatos, parametro))
                    
            # SUB-OPCIÓN 6: volver
            elif sub_opcion == '6':
                break
                    
            else:
                print("Introduce una opción válida.")
    
    # OPCIÓN 4: buscar temperamento --------------------------
    elif opcion == '4':
        while True:
            print("\n" + "ADJETIVOS DISPONIBLES" + "-"*30 + "\n")
            mostrar_menu_temperamento()
            respuesta = input("\nElige un adjetivo (1-9): ")
            palabra = ''
            
            if respuesta == "1":
                palabra = "solitario"
                
            elif respuesta == "2":
                palabra = "territorial"
                
            elif respuesta == "3":
                palabra = "tranquilo"
                
            elif respuesta == "4":
                palabra = "activo"
            
            elif respuesta == "5":
                palabra = "dócil"
            
            elif respuesta == "6":
                palabra = "rápido"
                
            elif respuesta == "7":
                palabra = "tímido"
                
            elif respuesta == "8":
                palabra = "Propenso a morder"
            
            elif respuesta == "9":
                break
            
            else:
                print("Introduce una opción válida")
            
            if palabra: 
                print(procesar_datos.buscar_temperamento(cargarDatos, palabra))
            
    else:
        print("Opción no válida.")
        