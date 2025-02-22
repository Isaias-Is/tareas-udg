from administrador import Administrador, Materia

admin = Administrador()

# admin.agregarMateriaAleatoria()
# admin.agregarMateriaAleatoria()
# admin.agregarMateriaAleatoria()
# admin.mostrarMaterias()
# admin.mostrarTablaMaterias()

# admin.respaldar("materias")

# admin.recuperar("materias")
# admin.mostrarTablaMaterias()

# Falta la implementación del menú.
def menu():
    while True:
        print("-" * 35)
        print(f"{"MENÚ":^35}")
        print("-" * 35)
        print("1. Agregar materia")
        print("2. Generar y agregar materia aleatoria")
        print("3. Mostrar representación de materias")
        print("4. Mostrar tabla de materias")
        print("5. Respaldar materias")
        print("6. Recuperar materias")
        print("7. Salir")
        print("-" * 35)
        op = int(input("Opción: "))

        if op == 1:
            print("-" * 10 + "Agregar materia" + "-" * 10)
            materia = Materia()
            materia.nombre = input("Ingrese el nombre de la materia: ")
            materia.clave = input("Ingrese la clave de la materia: ")[:5]
            materia.carrera = input("Ingrese la carrera de la materia: ")[-4:]
            materia.creditos = int(input("Ingrese los créditos de la materia: "))
            admin.agregarMateria(materia)
        elif op == 2:
            admin.agregarMateriaAleatoria()
            print("Materia aleatoria agregada")
        elif op == 3:
            print("-" * 10 + "Materias" + "-" * 10)
            admin.mostrarMaterias()
        elif op == 4:
            print("-" * 10 + "Tabla de Materias" + "-" * 10)
            admin.mostrarTablaMaterias()
        elif op == 5:
            admin.respaldar("materias")
            print("Materias respaldadas")
        elif op == 6:
            admin.recuperar("materias")
            print("Materias recuperadas")
        elif op == 7:
            print("Saliendo del programa...")
            return 1
        else:
            print("Opción inválida")
        

if __name__ == "__main__":
    menu()