#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <fstream>
#include <chrono>
#include "json.hpp"

using json = nlohmann::json;
using namespace std;
using namespace std::chrono;

// -----------------------------------------------
// Estructura para almacenar el grafo:
// - Usamos un 'unordered_map' (tabla hash) para eficiencia
// - Cada nodo (int) apunta a un vector de pares:
//   - primer elemento del par: nodo destino (int)
//   - segundo elemento: peso de la arista (int)
// -----------------------------------------------
unordered_map<int, vector<pair<int, int>>> grafo;

// -----------------------------------------------
// Implementación del algoritmo de Dijkstra
// - inicio: nodo de partida (origen)
// - n_nodos: cantidad total de nodos en el grafo
// - Retorna: vector con las distancias mínimas desde el origen
// -----------------------------------------------
vector<int> dijkstra(int inicio, int n_nodos) {
    // 1. Inicialización de distancias:
    // - Todas empiezan en INT_MAX (infinito) excepto el origen que es 0
    vector<int> dist(n_nodos, INT_MAX);
    dist[inicio] = 0;

    // Cola de prioridad (min-heap) para obtener siempre el nodo más cercano
    // - Almacena pares: (distancia acumulada, nodo)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    pq.push({0, inicio});

    // 2. Procesamiento principal
    while (!pq.empty()) {
        // Extraemos el nodo con menor distancia acumulada
        int u = pq.top().second;  // Nodo actual
        int d = pq.top().first;   // Distancia acumulada hasta u
        pq.pop();

        // Si ya encontramos un camino mejor, lo ignoramos
        if (d > dist[u]) continue;

        // 3. Relajación de aristas:
        // - Recorremos todos los vecinos del nodo actual
        for (auto& [v, w] : grafo[u]) {
            // Si la distancia actual + peso de la arista es mejor que la conocida:
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;  // Actualizamos la distancia
                pq.push({dist[v], v});   // Agregamos a la cola para procesar
            }
        }
    }
    return dist;
}

int main() {
    // -----------------------------------------------
    // Configuración inicial
    // -----------------------------------------------
    const string archivo_json = "grafo_10nodos.json";  // Archivo a cargar
    const int nodo_origen = 0;  // Nodo desde donde calculamos las distancias

    // -----------------------------------------------
    // Carga del grafo desde el archivo JSON
    // -----------------------------------------------
    ifstream file(archivo_json);
    json data = json::parse(file);  // Parseamos el JSON

    // Convertimos los datos del JSON a nuestra estructura de grafo
    for (auto& [nodo_str, vecinos] : data.items()) {
        int u = stoi(nodo_str);  // Convertimos el nombre del nodo a entero

        for (auto& par : vecinos) {
            // Manejo seguro de tipos (por si el JSON tiene números como strings)
            int v = par[0].is_string() ? stoi(par[0].get<string>()) : par[0].get<int>();
            int w = par[1].is_string() ? stoi(par[1].get<string>()) : par[1].get<int>();

            grafo[u].emplace_back(v, w);  // Añadimos la conexión al grafo
        }
    }

    // -----------------------------------------------
    // Ejecución del algoritmo y medición de tiempo
    // -----------------------------------------------
    auto inicio = high_resolution_clock::now();  // Iniciamos cronómetro

    vector<int> distancias = dijkstra(nodo_origen, data.size());  // Ejecutamos Dijkstra

    auto fin = high_resolution_clock::now();  // Detenemos cronómetro

    // -----------------------------------------------
    // Mostramos resultados
    // -----------------------------------------------
    cout << "Distancias minimas desde el nodo " << nodo_origen << ":\n";
    for (size_t i = 0; i < distancias.size(); ++i) {
        cout << "Nodo " << i << ": ";
        if (distancias[i] == INT_MAX) {
            cout << "Inalcanzable";
        } else {
            cout << distancias[i];
        }
        cout << "\n";
    }

    // Calculamos y mostramos el tiempo de ejecución
    auto duracion = duration_cast<microseconds>(fin - inicio);
    cout << "\nTiempo de ejecucion: " << duracion.count() << " microsegundos\n";

    return 0;
}
