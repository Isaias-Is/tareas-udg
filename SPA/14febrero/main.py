import json
from pprint import pprint

dic = {}

def agregar():
    print("-" * 5 + "Agregar país-capital" + "-" * 5)
    pais = input("País: ").strip()
    capital = input("Capital: ")
    if pais in dic:
        dic[pais].append(capital)
        return
    dic[pais] = [capital]

def mostrar():
    print("-" * 5 + "Mostrar con pprint" + "-" * 5)
    pprint(dic, width=4)

def respaldar():
    with open("dic.json", "w") as archivo:
        json.dump(dic, archivo)
    print("Datos respaldados...")

def recuperar():
    global dic
    dic.clear()
    with open("dic.json", "r") as archivo:
        dic = json.load(archivo)
    print("Datos recuperados...")

def consultar():
    print("-" * 5 + "Consultar capital de país" + "-" * 5)
    pais = input("País: ")
    if pais in dic:
        print(dic[pais])
    else:
        print("País inexistente")

def mostrarPaises():
    print("-" * 5 + "Mostrar países" + "-" * 5)
    cont = 0 
    for pais in dic.keys():
        cont += 1
        if cont < len(dic):
            print(pais, end=", ")
            continue
        print(pais)

def mostrarCapitales():
    print("-" * 5 + "Mostrar capitales" + "-" * 5)
    cont = 0 
    for capital in dic.values():
        cont += 1
        if cont < len(dic):
            print(capital, end=", ")
            continue
        print(capital)

def mostrarPaisesYCapitales():
    print("-" * 5 + "Mostrar paises y capitales" + "-" * 5)
    print(f"{'Países':<12}{'Capitales':<12}")
    print("-" * 25)
    for val in dic.items():
        print(f"{val[0]:<12}", end="")
        for v in val[1]:
            print(f"{v:<12}")

def eliminarPais():
    print("-" * 5 + "Eliminar pais" + "-" * 5)
    pais = input("Pais: ")
    if pais in dic:
        del dic[pais] #Del elimina la pais y su capital.
    else:
        print("País inexistente")

def modificarDic():
    print("-" * 5 + "Modificar" + "-" * 5)
    pais = input("País: ")
    if pais in dic:
        capital = input("Nuevo capital: ")
        dic[pais] = [capital]
    else:
        print("País inexistente")

def vaciar():
    dic.clear()
    print("Diccionario vaciado...")

def main():
    while True:
        print("-" * 30)
        print(f"{'MENÚ':^30}")
        print("-" * 30)
        print("1. Agregar país-capital")
        print("2. Mostrar")
        print("3. Respaldar")
        print("4. Recuperar")
        print("5. Consultar")
        print("6. Mostrar Países")
        print("7. Mostrar Capitales")
        print("8. Mostrar Países y Capitales")
        print("9. Eliminar pais")
        print("10. Modificar")
        print("11. Vaciar")
        print("0. Salir")
        op = int(input("Opción: "))

        if op == 1:
            agregar()
        elif op == 2:
            mostrar()
        elif op == 3:
            respaldar()
        elif op == 4:
            recuperar()
        elif op == 5:
            consultar()
        elif op == 6:
            mostrarPaises()
        elif op == 7:
            mostrarCapitales()
        elif op == 8:
            mostrarPaisesYCapitales()
        elif op == 9:
            eliminarPais()
        elif op == 10:
            modificarDic()
        elif op == 11:
            vaciar()
        elif op == 0:
            print("Saliendo del programa...")
            break;

if __name__ == "__main__":
    main()