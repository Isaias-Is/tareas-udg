from enum import auto
from turtle import onclick
from punto import Punto, AdministradorPuntos
from nicegui import ui

admin = AdministradorPuntos()

def agregar_punto():
        punto = Punto(int(x_input.value), int(y_input.value), int(radio_input.value), [int(r_input.value), int(g_input.value), int(b_input.value)])
        admin.insertar_al_final(punto)
        ui.notify(f"Punto agregado: {punto.a_diccionario()}", type='positive')

def ordenar_tabla_puntos(atributo: str):
    admin.ordenar_por(atributo)
    tabla.update_rows([punto.a_diccionario() for punto in admin.puntos])

with ui.tabs().classes('fixed-bottom bg-[#39393A]') as tabs:
    crearPuntos_tab = ui.tab("Añadir Puntos", icon='add_location').classes('text-white')
    mostrarPuntos_tab = ui.tab("Mostrar Puntos", icon='table_view').classes('text-white')
    guardarPuntos_tab = ui.tab("Guardar/Recuperar", icon='cloud_download').classes('text-white')

with ui.tab_panels(tabs).classes('fixed-center'):
    with ui.tab_panel(crearPuntos_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Datos del punto").classes('text-xl font-bold')
            x_input = ui.input("X", placeholder="Coordenada X (0-500)", validation='number', range=(0, 500))
            y_input = ui.input("Y", placeholder="Coordenada Y (0-500)", validation='number', range=(0, 500))
            radio_input = ui.input("Radio", placeholder="Radio (5-50)", validation='number', range=(5, 50))
            r_input = ui.input("R", placeholder="Rojo (0-255)", validation='number', range=(0, 255))
            g_input = ui.input("G", placeholder="Verde (0-255)", validation='number', range=(0, 255))
            b_input = ui.input("B", placeholder="Azul (0-255)", validation='number', range=(0, 255))
            with ui.row().classes('gap-4'):
                ui.button("Agregar Punto", on_click=agregar_punto)
                ui.button("Limpiar Campos").on('click', lambda: [x_input.clear(), y_input.clear(), radio_input.clear(), r_input.clear(), g_input.clear(), b_input.clear()])
                ui.button("Crear 10 Puntos Aleatorios", on_click=lambda: (admin.insertar_al_final(punto) for punto in [admin.generar() for _ in range(10)]))
            
    with ui.tab_panel(mostrarPuntos_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Tabla de Puntos").classes('text-xl font-bold')
            tabla = ui.table(columns=[{'name': 'id', 'label': 'ID', 'field': 'id'},
                                       {'name': 'x', 'label': 'X', 'field': 'x'},
                                       {'name': 'y', 'label': 'Y', 'field': 'y'},
                                       {'name': 'radio', 'label': 'Radio', 'field': 'radio'},
                                       {'name': 'color', 'label': 'Color (R,G,B)', 'field': 'color'},
                                       ], rows=[punto.a_diccionario() for punto in admin.puntos])
            with ui.row().classes('gap-2 justify-center'):
                ui.button("Mostrar", on_click=lambda: tabla.update_rows([punto.a_diccionario() for punto in admin.puntos]))
                ui.button("Limpiar Datos y Tabla", on_click=lambda: tabla.update_rows([]) or admin.limpiar())
            ui.label("Ordenar Datos").classes('text-base font-bold')
            with ui.row().classes('gap-2 justify-center'):
                with ui.dropdown(label="Ordenar por", auto_close="True"):
                    ui.item('ID', onclic=lambda: ordenar_tabla_puntos('id'))
                    ui.item('X', onclic=lambda: ordenar_tabla_puntos('x'))
                    ui.item('Y', onclic=lambda: ordenar_tabla_puntos('y'))
                    ui.item('Radio', onclic=lambda: ordenar_tabla_puntos('radio'))
                    ui.item('Color', onclic=lambda: ordenar_tabla_puntos('color'))
                with ui.dropdown(label="Orden", auto_close="True"):
                    ui.item('Ascendente', onclic=lambda: ordenar_tabla_puntos('ascendente'))
                    ui.item('Descendente', onclic=lambda: ordenar_tabla_puntos('descendente'))
            agregar_btn = ui.button("Agregar Punto").on('click', agregar_punto)
ui.run(title="Puntos", reload=True, port=8080)