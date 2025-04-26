from algoritmos import puntos_mas_cercanos
from grafos import Grafo
from punto import Punto, AdministradorPuntos
from nicegui import ui
import matplotlib.pyplot as plt
import re
from pprint import pprint

admin = AdministradorPuntos()
grafo = Grafo(admin.puntos)
regex = re.compile(r'\b([0-9]|[1-9][0-9]|[1-4][0-9][0-9]|500)\b')

def actualizar_lista_conexiones():
    if admin.puntos.__len__() < 2:
        ui.notify("Debe haber al menos 2 puntos para crear una conexión", type='negative', position="bottom-center")
        return
    punto1_select.set_options({punto: str(punto) for punto in admin.puntos if punto != punto2_select.value}, value=punto1_select.value)
    punto2_select.set_options({punto: str(punto) for punto in admin.puntos if punto != punto1_select.value}, value=punto2_select.value)

def operacion_conexion(op: int):
    try:
        if op == 1:
            grafo.agregar_conexion(punto1_select.value, punto2_select.value)
            ui.notify("Conexión creada", type='positive', position="bottom-right")
        elif op == 2:
            grafo.eliminar_conexion(punto1_select.value, punto2_select.value)
            ui.notify("Conexión eliminada", type='positive', position="bottom-right")
    except ValueError as e:
        ui.notify(str(e), type='negative', position="bottom-right")
        return
    actualizar_grafo()

def actualizar_grafo():
    limpiar_grafica()
    plt.title("Grafo")
    grafo.checar_nuevos_puntos(admin.puntos)
    with conexiones_plot:
        for punto in admin.puntos:
            plt.scatter(punto.x, punto.y, s=punto.radio, color=[punto.color[0]/255, punto.color[1]/255, punto.color[2]/255], alpha=0.7)
            plt.text(punto.x, punto.y, str(punto), ha="center", va='center')
        for punto, conexiones in grafo.grafo.items():
            for conexion in conexiones:
                plt.plot([punto.x, conexion.x], [punto.y, conexion.y], color=[punto.color[0]/255, punto.color[1]/255, punto.color[2]/255], linewidth=1)

def limpiar_grafica():
    plt.cla()
    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.xlabel('x')
    plt.ylabel('y')

def dibujarPuntos():
    limpiar_grafica()
    plt.title("Puntos")
    with puntos_plot:
        for punto in admin.puntos:
            plt.scatter(punto.x, punto.y, s=punto.radio, color=[punto.color[0]/255, punto.color[1]/255, punto.color[2]/255], alpha=0.7)

def dibujarPuntosMasCercanos(puntos_mas_cercanos):
    if puntos_mas_cercanos is None:
        ui.notify("Debe haber agregados mínimo 2 puntos", type='negative', position="bottom-right")
        return
    limpiar_grafica()
    plt.title("Puntos")
    with puntos_plot:
        dibujarPuntos()
        #print("Conectando puntos más cercanos...")
        for par in puntos_mas_cercanos:
            plt.plot([par.punto1.x, par.punto2.x], [par.punto1.y, par.punto2.y], color=(par.punto1.color[0]/255, par.punto1.color[1]/255, par.punto1.color[2]/255), alpha=0.5)

def limpiar_campos():
    x_input.value = ""
    y_input.value = ""
    radio_input.value = ""
    r_input.value = ""
    g_input.value = ""
    b_input.value = ""

def agregar_punto():
        punto = Punto(int(x_input.value), int(y_input.value), int(radio_input.value), [int(r_input.value), int(g_input.value), int(b_input.value)])
        admin.insertar_al_final(punto)
        tabla.update_rows([punto.a_diccionario() for punto in admin.puntos])

def ordenar_tabla_puntos(atributo: str, orden: int = 0):
    if orden == 0:
        orden = 'ascendente'
    else:
        orden = 'descendente'
    admin.ordenar_por(atributo, orden)
    tabla.update_rows([punto.a_diccionario() for punto in admin.puntos])

with ui.header().classes('bg-[#E6E6E6] justify-center'):
    ui.label('Administrador de Puntos').style('color: #39393A; font-size: 36px; font-weight: bold;')

with ui.tabs().classes('fixed-bottom bg-[#297373]') as tabs:
    crear_puntos_tab = ui.tab("Añadir Puntos", icon='add_location').classes('text-white')
    mostrar_puntos_tab = ui.tab("Mostrar Puntos", icon='table_view').classes('text-white')
    grafica_tab = ui.tab("Gráfica", icon='show_chart').classes('text-white')
    graficar_conexiones_tab = ui.tab("Conexiones", icon='share').classes('text-white').on("click", lambda: actualizar_lista_conexiones() or actualizar_grafo())
    guardar_recuperar_tab = ui.tab("Guardar/Recuperar", icon='cloud_download').classes('text-white')

with ui.tab_panels(tabs).classes('fixed-center'):
    with ui.tab_panel(crear_puntos_tab).classes('bg-gray-100'):
        with ui.card():
            ui.label("Datos del punto").classes('text-xl font-bold')
            x_input = ui.input("X", placeholder="Coordenada X (0-500)", validation={'El número debe estar entre 0 y 500.': lambda val: regex.search(val) is not None}).style('width: 100%')
            y_input = ui.input("Y", placeholder="Coordenada Y (0-500)", validation={'El número debe estar entre 0 y 500.': lambda val: regex.search(val) is not None}).style('width: 100%')
            radio_input = ui.input("Radio", placeholder="Radio (5-50)", validation=lambda val: "El número debe estar entre 5 y 50." if regex.search(val) is None else None).style('width: 100%')
            r_input = ui.input("R", placeholder="Rojo (0-255)", validation={'El número debe estar entre 0 y 255.': lambda val: regex.search(val) is not None}).style('width: 100%')
            g_input = ui.input("G", placeholder="Verde (0-255)", validation={'El número debe estar entre 0 y 255.': lambda val: regex.search(val) is not None}).style('width: 100%')
            b_input = ui.input("B", placeholder="Azul (0-255)", validation={'El número debe estar entre 0 y 255.': lambda val: regex.search(val) is not None}).style('width: 100%')
            ui.button("Agregar Punto", on_click=lambda: agregar_punto() or ui.notify("Punto agregado", type='positive', position="bottom-right")).classes('justify-self-center w-full')
            ui.button("Limpiar Campos", on_click=lambda: limpiar_campos()).classes('justify-self-center w-full')
            ui.button("Crear 10 Puntos Aleatorios", on_click=lambda: (admin.insertar_al_final(punto) for punto in [admin.generar() for _ in range(10)]) and tabla.update_rows([punto.a_diccionario() for punto in admin.puntos]) or ui.notify("10 puntos aleatorios creados", type='positive', position="bottom-right")).classes('justify-self-center w-full')
            
    with ui.tab_panel(mostrar_puntos_tab).classes('bg-gray-100'):
        with ui.card().classes('justify-center'):
            ui.label("Tabla de Puntos").classes('text-xl font-bold')
            tabla = ui.table(columns=[{'name': 'id', 'label': 'ID', 'field': 'id'},
                                       {'name': 'x', 'label': 'X', 'field': 'x'},
                                       {'name': 'y', 'label': 'Y', 'field': 'y'},
                                       {'name': 'radio', 'label': 'Radio', 'field': 'radio'},
                                       {'name': 'color', 'label': 'Color (R,G,B)', 'field': 'color'},
                                       ], rows=[punto.a_diccionario() for punto in admin.puntos])
            ui.label("Ordenar Datos").classes('text-base font-bold')
            with ui.row().classes('gap-2 justify-center'):
                ui.button("Mostrar", on_click=lambda: tabla.update_rows([punto.a_diccionario() for punto in admin.puntos]))
                ui.button("Limpiar Datos y Tabla", on_click=lambda: tabla.update_rows([]) or admin.limpiar())
            with ui.row().classes('gap-2 justify-center items-center'):
                orden_select = ui.select(label="Ordenar por:", options={'id':'ID', 'x':'X', 'y':'Y', 'radio':'Radio', 'color':'Color'}, on_change=lambda e: ordenar_tabla_puntos(e.value, orden_checkbox.value)).style('width: 100px')
                orden_select.style('width: 100px')
                orden_select.set_value('id')
                orden_checkbox = ui.checkbox(on_change= lambda: ordenar_tabla_puntos(orden_select.value, orden_checkbox.value))
                ui.label("Orden Descendente").classes('align-center')
    with ui.tab_panel(grafica_tab).classes('bg-gray-100'):
        with ui.card().classes('justify-center'):
            ui.label("Gráfica").classes('text-xl font-bold')
            with ui.pyplot(figsize=(5,5), close=False).style('height: 600px') as puntos_plot:
                limpiar_grafica()
                plt.title("Puntos")
            with ui.row().classes('w-full justify-center items-center'):
                ui.button("Dibujar Puntos", on_click=dibujarPuntos)
                ui.button("Conectar Puntos Más Cercanos", on_click=lambda: dibujarPuntosMasCercanos(puntos_mas_cercanos(admin.puntos)))

    with ui.tab_panel(graficar_conexiones_tab).classes('bg-gray-100'):
        with ui.card().classes('justify-center'):
            ui.label("Conexiones").classes('text-xl font-bold')
            with ui.pyplot(figsize=(5,5), close=False).style('height: 600px') as conexiones_plot:
                limpiar_grafica()
                plt.title("Grafo")
            with ui.row().classes('w-full justify-center items-center'):
                punto1_select = ui.select({punto: str(punto) for punto in admin.puntos}, label="Punto 1", on_change=lambda: actualizar_lista_conexiones()).classes('w-1/4')
                ui.label("conectar con")
                punto2_select = ui.select({punto: str(punto) for punto in admin.puntos}, label="Punto 2", on_change=lambda: actualizar_lista_conexion()).classes('w-1/4')
            with ui.row().classes('w-full justify-center items-left'):
                ui.button("Conectar", on_click=lambda: operacion_conexion(1) or actualizar_grafo())
                ui.button("Eliminar Conexión", on_click=lambda: operacion_conexion(2) or actualizar_grafo())

    with ui.tab_panel(guardar_recuperar_tab).classes('bg-gray-100'):
        with ui.card().classes('text-center justify-center items-center'):
            ui.label("Guardar/Exportar/Importar").classes('text-x1 font-bold')
            ui.button("Guardar", on_click=lambda: admin.respaldar('puntos.csv') or ui.notify("Archivo guardado existosamente", type='positive', position="bottom-right")).style('width: 125px')
            ui.button("Exportar", on_click=lambda: ui.download('puntos.csv')).style('width: 125px')
            ui.upload(on_upload= lambda evento: admin.cargar(evento) or tabla.update_rows([i.a_diccionario() for i in admin.puntos])
                      or ordenar_tabla_puntos(orden_select.value, orden_checkbox.value) or ui.notify("Carga terminada", type='positive', position="bottom-rigth")).style('width: 125px')

            
tabs.set_value('Añadir Puntos')
ui.run(title="Puntos", reload=True, port=8080)