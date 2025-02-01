from administrador import Administrador

admin = Administrador()

while True:
    print("---------Menú-------------")
    print("1. Agregar tanque")
    print("2. Mostrar tanques")
    print("3. Salir")
    op = input("---------------\nOpción: ")
    if op == "1":
        admin.agregarTanque()
    elif op == "2":
        admin.mostrarTanques()
    else:
        break

