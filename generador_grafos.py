import json
import random
from pathlib import Path

def generar_grafo(n_nodos):
    """Genera un grafo aleatorio con pesos entre 1-60 minutos"""
    return {
        str(i): [
            (str(j), random.randint(1, 60)) #asigna un peso aleatorio entre 1 y 60 a cada conexión.
            for j in random.sample(range(n_nodos), min(5, n_nodos)) #selecciona hasta 5 nodos vecinos distintos al azar.
            if j != i  # La condición if j != i evita que un nodo se conecte a sí mismo.
        ]
        for i in range(n_nodos)
    }

# Generar los 3 archivos JSON
tamanios = [10, 100, 1000]
for n in tamanios:
    ruta = Path(f"grafo_{n}nodos.json")
    with open(ruta, 'w', encoding='utf-8') as f:  #with open(...) as f asegura que el archivo se cierre automáticamente.
        json.dump(generar_grafo(n), f, indent=2) #convierte el diccionario Python a formato JSON.   indent=2 hace que el archivo sea legible para humanos (con sangrías).
    print(f"✅ grafo_{n}nodos.json generado")

print("\n¡Todos los archivos creados con éxito!")