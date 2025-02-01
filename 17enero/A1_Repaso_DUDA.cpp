// Autor: Isaias Aldama
// Fecha: 22 de enero de 2025
/*Descripción: Este programa permite almacenar tanques en un arreglo de estructura, guardarlos en un archivo CSV
    y cargarlos desde el archivo generados cuando se vuelva a correr el programa.
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// Vars globales.
int cont = -1;
int op = 0;

struct Tanque
{
    string nombre;
    int salud;
    int dano;
    float vel;
} tanques[5];

int anadirTanque(void)
{
    if (cont > 3)
    {
        cout << "Ya no hay capacidad para almacenar más tanques.\nATENCIÓN: Si continua el nuevo tanque que agrege reemplazará al último tanque almacenado." << "\n";
        cout << "¿Desea continuar? (1: Sí, 0: No): ";
        cin >> op;
        if (op == 0)
            return 0;
        cont = 3;
    }

    cont++;
    cout << "--------AÑADIR TANQUE--------" << "\n";
    string temp = "";
    cout << "Nombre del Tanque: ";
    cin >> tanques[cont].nombre;
    cout << "Salud: ";
    cin >> tanques[cont].salud;
    cout << "Daño: ";
    cin >> tanques[cont].dano;
    cout << "Velocidad: ";
    cin >> tanques[cont].vel;

    return 1;
}

int eliminarTanque(void)
{
    if (cont < 0)
    {
        cout << "No hay tanques almacenados en este momento." << "\n";
        return -1;
    }

    cout << "--------ELIMINAR TANQUE--------" << "\n";
    cout << "Esta acción eliminará el último tanque almacenado. ¿Desea proceder de todos modos?\n(1: Sí, 0: No): ";
    cin >> op;
    if (op == 0)
        return 0;

    cont--;
    return 1;
}

int mostrarTanques(void)
{
    if (cont < 0)
    {
        cout << "No hay tanques almacenados en este momento." << "\n";
        return -1;
    }

    cout << "--------TANQUES ALMACENADOS--------" << "\n";
    for (int i = 0; i <= cont; i++)
    {
        cout << "Tanque " << i + 1 << ":\n";
        cout << "Nombre: " << tanques[i].nombre << "\n";
        cout << "Salud: " << tanques[i].salud << "\n";
        cout << "Daño: " << tanques[i].dano << "\n";
        cout << "Velocidad: " << tanques[i].vel << "\n";
    }

    return 1;
}

int guardarCSV(void)
{
    if (cont < 0)
    {
        cout << "No hay tanques almacenados en este momento." << "\n";
        return -1;
    }

    ofstream archivo("tanques.csv");
    cout << "--------GUARDAR CSV--------" << "\n";
    cout << "Guardando CSV..." << "\n";
    if (!archivo.is_open())
    {
        cout << "Ocurrio un error al crear el CSV." << "\n";
        return -1;
    }
    for (int i = 0; i <= cont; i++)
    {
        archivo << tanques[i].nombre << "," << tanques[i].salud << "," << tanques[i].dano << "," << tanques[i].vel << "\n";
    }
    cout << "Guardado exitoso!" << "\n";
    archivo.close(); // Imperativo cerrar el stream de datos.

    return 1;
}

int cargarCSV(void)
{
    ifstream archivo("tanques.csv");
    cout << "--------CARGAR CSV--------" << "\n";
    cout << "Cargando CSV..." << "\n";
    if (!archivo.is_open())
    {
        cout << "Ocurrio un error al cargar el CSV." << "\n";
        return -1;
    }
    string temp;
    for (cont = 0; cont < 5; cont)
    {
        getline(archivo, temp, ',');
        cout << temp << "\n";
        if (archivo.eof()) {
            cout << "EOF Alcanzado." << "\n";
            cont--;
            break;
        }
        tanques[cont].nombre = temp;
        getline(archivo, temp, ',');
        tanques[cont].salud = stoi(temp);
        getline(archivo, temp, ',');
        tanques[cont].dano = stoi(temp);
        getline(archivo, temp, '\n');
        tanques[cont].vel = stof(temp);
        cont++;
    }
    cout << "Carga exitosa!" << "\n";
    archivo.close(); // Imperativo cerrar el stream de datos.
    return 1;
}

int main()
{
    while (true)
    {
        cout << "----------------MENÚ---------------" << "\n";
        cout << "- 1. Añadir tanque al final." << "\n";
        cout << "- 2. Eliminar último tanque." << "\n";
        cout << "- 3. Mostrar tanques almacenados." << "\n";
        cout << "- 4. Guardar lista de tanques en CSV." << "\n";
        cout << "- 5. Cargar datos desde un CSV." << "\n";
        cout << "- 6. Salir." << "\n";
        cout << "-----------------------------------" << "\n";
        cout << "Opción: ";
        cin >> op;

        switch (op)
        {
        case 1:
            anadirTanque();
            break;
        case 2:
            eliminarTanque();
            break;
        case 3:
            mostrarTanques();
            break;
        case 4:
            guardarCSV();
            break;
        case 5:
            cargarCSV();
            break;
        case 6:
            return 1;
        default:
            cout << "Opción no válida." << "\n";
            break;
        }
    }
    return 0;
}