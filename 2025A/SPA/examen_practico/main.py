from nicegui import ui
from bicipuerto import Bicipuerto, Bici

bicipuerto = Bicipuerto()
bicipuerto.ingresar_bici(Bici(10, 1760, 1))
bicipuerto.ingresar_bici(Bici(60, 5410, 2))
bicipuerto.ingresar_bici(Bici(1, 100, 3))

def ingresar_bici():
    try:
        bici = Bici(int(tiempo_input.value), int(metros_input.value), int(id_input.value))
        bicipuerto.ingresar_bici(bici)
    except ValueError:
        print("Error: Los valores ingresados no son válidos.")
        ui.notify("Los valores deben de ser enteros positivos.", type='negative')

def limpiar_campos():
    tiempo_input.value = ""
    metros_input.value = ""
    id_input.value = ""

def menu():
    while True:
        print(f"{"BICIPUERTO":^25}")
        print("-" * 25)
        print("1. Ingresar bicicleta")
        print("2. Mostrar tabla de bicicletas")
        print("0. Salir") 
        op = int(input("Opción: "))
        if op == 1:
            print("-" * 5 + "Ingresando Bicicleta al Bicipuerto" + "-" * 5)
            id = int(input("ID: "))
            tiempo = int(input("Horas de uso: "))
            metros = int(input("Metros recorridos: "))
            res = bicipuerto.ingresar_bici(Bici(tiempo, metros, id))
            if res == 0:
                print("La información de la bicicleta ha sido actualizada.")
            else:
                print("Nuevo ingreso exitoso.")
        elif op == 2:
            bicipuerto.mostrar_tabla_bicis()
        elif op == 0:
            print("Saliendo...")
            return
        else:
            print("Opción inválida")

# Interfaz de usuario web.
with ui.tabs().classes('fixed-bottom bg-[#00953b]') as tabs:
    ingresarBici_tab = ui.tab("Ingresar Bicicleta", icon='directions_bike').classes('text-white')
    mostrarBicis_tab = ui.tab("Mostrar Bicicletas", icon='table_view').classes('text-white')
    guardar_recuperar_tab = ui.tab("Guardar/Recuperar", icon='cloud_download').classes('text-white')

with ui.tab_panels(tabs).classes('fixed-center'):
    with ui.tab_panel(ingresarBici_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Ingrese los datos de la bicicleta").classes('text-xl font-bold')
            id_input = ui.input("ID", placeholder="ID de la bicicleta", validation='number')
            tiempo_input = ui.input("Horas de uso", placeholder="Horas de uso de la bicicleta", validation='number')
            metros_input = ui.input("Metros recorridos", placeholder="Metros recorridos en la bicicleta", validation='number')
            with ui.row().classes('gap-2 justify-center'):
                ui.button("Ingresar", on_click=lambda: ingresar_bici() or tabla.update_rows([i.to_dict() for i in bicipuerto.bicis]))
                ui.button("Limpiar Campos", on_click=limpiar_campos)
    with ui.tab_panel(mostrarBicis_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Bicicletas del Bicipuerto").classes('text-xl font-bold')
            tabla = ui.table(columns=[{'name': 'id', 'label': 'ID', 'field': 'id'},
                                      {'name': 'horasUso', 'label': 'Horas de Uso', 'field': 'horasUso'},
                                      {'name': 'metrosRecorridos', 'label': 'Metros Recorridos', 'field': 'metrosRecorridos'},
                                      ], rows=[i.to_dict() for i in bicipuerto.bicis])
            with ui.row().classes('gap-2 justify-center'):
                ui.button("Mostrar", on_click= lambda: tabla.update_rows([i.to_dict() for i in bicipuerto.bicis]))
                ui.button("Vaciar Bicipuerto", on_click= lambda: tabla.update_rows([]) or bicipuerto.bicis.clear())

    with ui.tab_panel(guardar_recuperar_tab).classes('bg-gray-100'):
        with ui.card().classes('text-center justify-center items-center'):
            ui.label("Guardar/Exportar/Importar").classes('text-x1 font-bold')
<<<<<<< HEAD
            ui.button("Guardar", on_click=lambda: bicipuerto.respaldarCSV('bicipuertoCSV') or ui.notify("Archivo guardado existosamente", type='positive')).style('width: 125px')
            ui.button("Exportar", on_click=lambda: ui.download('bicipuertoCSV.csv')).style('width: 125px')
=======
            ui.button("Guardar", on_click=lambda: bicipuerto.respaldarCSV('materiaCSV') or ui.notify("Archivo guardado existosamente", type='positive')).style('width: 125px')
            ui.button("Exportar", on_click=lambda: ui.download('materiaCSV.csv')).style('width: 125px')
>>>>>>> 76e249621f6c131900a3729dc57913c70910d2be
            ui.upload(on_upload= lambda evento: bicipuerto.cargarCSV(evento) or tabla.update_rows([]) or tabla.update_rows([i.to_dict() for i in bicipuerto.bicis])
                      or ui.notify("Carga terminada", type='positive')).style('width: 125px')

            pass

#menu()
tabs.set_value('Mostrar Bicicletas')
ui.run(port=8001)