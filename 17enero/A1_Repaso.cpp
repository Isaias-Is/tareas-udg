#include <iostream>
#include <string>

using namespace std;

// Vars globales.
int cont = 0;

struct Tanque {
    string nombre;
    int salud;
    int dano;
    float vel;
} tanques[5];

int anadirTanque(void) {
    if (cont > 3) cont = 3;

    cont++;
    cout << "--------AÑADIR TANQUE--------" << "\n";
    cout << "Nombre del Tanque: ";
    cin << tanques[cont].nombre;
    cout << "Salud: ";
    cin << tanques[cont].salud;
    cout << "Daño: ";
    cin << tanques[cont].dano;
    cout << "Velocidad: ";
    cin << tanques[cont].vel;

    return 1;
}

int main() {
    int op = 0;
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

    return 1;
}