# Importamos las bibliotecas necesarias
import heapq  # Para usar la cola de prioridad (implementación de min-heap)
import json  # Para leer el archivo JSON con el grafo
import time  # Para medir el tiempo de ejecución
from pathlib import Path  # Para manejo moderno de rutas de archivos


def dijkstra(grafo, inicio):
    """Implementación del algoritmo de Dijkstra para caminos más cortos.

    Args:
        grafo (dict): Diccionario que representa el grafo {nodo: [(vecino, peso), ...]}
        inicio (str): Nodo de partida para el cálculo de distancias

    Returns:
        dict: Diccionario con las distancias mínimas desde el nodo inicio
    """
    # Inicializamos todas las distancias como infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    # La distancia al nodo de inicio es 0
    distancias[inicio] = 0

    # Creamos una cola de prioridad (min-heap) e insertamos el nodo inicial
    cola = [(0, inicio)]

    # Mientras haya nodos por procesar en la cola
    while cola:
        # Extraemos el nodo con la menor distancia actual
        d, u = heapq.heappop(cola)

        # Si ya encontramos un camino mejor a este nodo, lo ignoramos
        if d > distancias[u]:
            continue

        # Para cada vecino del nodo actual
        for v, w in grafo[u]:
            # Calculamos la distancia alternativa pasando por u
            distancia_alternativa = distancias[u] + w

            # Si encontramos un camino más corto
            if distancia_alternativa < distancias[v]:
                # Actualizamos la distancia
                distancias[v] = distancia_alternativa
                # Agregamos a la cola de prioridad
                heapq.heappush(cola, (distancias[v], v))

    return distancias


# =============================================================================
# Configuración y ejecución del algoritmo
# =============================================================================

# Archivo JSON que contiene el grafo (puede cambiarse a grafo_10nodos.json o grafo_1000nodos.json)
archivo_json = "grafo_100nodos.json"

# Nodo desde el cual calcularemos las distancias más cortas
nodo_origen = "0"

# Cargamos el grafo desde el archivo JSON
with open(archivo_json, 'r') as f:
    # Convertimos el JSON a un diccionario de Python
    # Aseguramos que tanto nodos como vecinos sean strings
    grafo = {
        str(k): [(str(v[0]), v[1]) for v in vecinos]
        for k, vecinos in json.load(f).items()
    }

# Medimos el tiempo de ejecución
inicio = time.perf_counter()  # Más preciso que time.time()
distancias = dijkstra(grafo, nodo_origen)
fin = time.perf_counter()

# =============================================================================
# Presentación de resultados
# =============================================================================

# Imprimimos un encabezado visual
print("\n" + "=" * 50)
print(f"RESULTADOS DIJKSTRA - {archivo_json}")
print("=" * 50)

# Mostramos el nodo de origen
print(f"Nodo origen: {nodo_origen}")

# Imprimimos las distancias mínimas encontradas
print("\nDistancias mínimas:")
for nodo, dist in distancias.items():
    # Mostramos "Inalcanzable" si no hay camino
    print(f"Nodo {nodo}: {dist if dist != float('inf') else 'Inalcanzable'}")

# Mostramos el tiempo de ejecución
print("\n" + "-" * 50)
print(f"Tiempo total: {(fin - inicio) * 1000:.2f} ms")  # Convertimos a milisegundos
print("=" * 50)