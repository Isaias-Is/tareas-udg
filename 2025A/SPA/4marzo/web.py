from nicegui import ui
from administrador import Administrador, Materia
from materia import generarMateriaAleatoria

admin =  Administrador()
admin.recuperar("materias")

def agregarMateria():
    mat = Materia()
    mat.nombre = nombre.value
    mat.clave = clave.value
    mat.carrera = carrera.value
    mat.creditos = int(creditos.value)
    admin.agregarMateria(mat)
    admin.mostrarTablaMaterias()
    actualizar_tabla()

def generarMateria():
    mat = generarMateriaAleatoria()
    admin.agregarMateria(mat)
    admin.mostrarTablaMaterias()
    actualizar_tabla()

def actualizar_tabla():
    tabla.update_rows([mat.to_dict() for mat in admin.materias])

def limpiar_tabla():
    tabla.update_rows([])

with ui.tabs().classes('fixed-bottom bg-emerald-600') as tabs:
    formulario_tab = ui.tab("Agregar Materias", icon='menu_book').classes('text-white')
    tabla_tab = ui.tab("Ver Materias", icon='table_view').classes('text-white')
    exportarImportar_tab = ui.tab("Exportar/Importar", icon='cloud_download').classes('text-white')

with ui.tab_panels(tabs).classes('fixed-center'):
    with ui.tab_panel(formulario_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Ingrese los datos de la materia").classes('text-x1 font-bold')
            nombre = ui.input("Nombre", placeholder="Nombre de la materia")
            clave = ui.input("Clave", placeholder="Clave de la materia")
            carrera = ui.input("Carrera", placeholder="Carrera de la materia")
            creditos = ui.input("Créditos", value=8, placeholder="Créditos de la materia")
            with ui.row():
                ui.button("Agregar", on_click=agregarMateria)
                ui.button("Generar", on_click=generarMateria)

    with ui.tab_panel(tabla_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Materias Registradas").classes('text-x1 font-bold')
            tabla = ui.table(columns=[{'name': 'nombre', 'label': 'Nombre', 'field': 'nombre'},
                                      {'name': 'clave', 'label': 'Clave', 'field': 'clave'},
                                      {'name': 'carrera', 'label': 'Carrera', 'field': 'carrera'},
                                      {'name': 'creditos', 'label': 'Creditos', 'field': 'creditos'},
                                      ], rows=[mat.to_dict() for mat in admin.materias])
            with ui.row():
                ui.button("Mostrar", on_click=actualizar_tabla)
                ui.button("Limpiar", on_click=limpiar_tabla)
                ui.button("Vaciar Admin", on_click=lambda: limpiar_tabla() or admin.materias.clear())

    with ui.tab_panel(exportarImportar_tab).classes('bg-gray-100'):
        with ui.card().classes('text-center'):
            ui.label("Guardar/Exportar/Importar").classes('text-x1 font-bold')
            ui.button("Guardar", on_click=guardar("materias"))
            ui.button("Exportar", on_click=lambda: ("materias"))
            ui.button("Importar", on_click=lambda: admin.recuperar("materias"))

tabs.set_value('Ver Materias')
ui.run(port=8001)
