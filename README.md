# AlgoritmodeDijkstra

# Algoritmo de Dijkstra - Implementación en C++ y Python

Este repositorio contiene implementaciones del algoritmo de Dijkstra en C++ y Python. El objetivo es comparar el rendimiento y el uso de recursos entre ambos lenguajes aplicando el algoritmo sobre grafos generados desde archivos JSON.

---

## 📁 Estructura del Proyecto

```
├── cpp/
│   └── dijkstra.cpp              # Implementación en C++
├── python/
│   └── dijkstra.py              # Implementación en Python
├── grafos/
│   ├── grafo_10nodos.json       # Grafo con 10 nodos
│   ├── grafo_100nodos.json      # Grafo con 100 nodos
│   └── grafo_1000nodos.json     # Grafo con 1000 nodos
└── README.md                    # Este archivo
```

---

## ⚙️ Requisitos

### Python
- Python 3.8 o superior
- Librerías estándar: `heapq`, `json`, `time`

### C++
- Compilador compatible con C++17
---

## 🚀 Cómo Ejecutar

### Python

```bash
cd python
python dijkstra.py
```

### C++

```bash
cd cpp
g++ -std=c++17 dijkstra.cpp -o dijkstra
./dijkstra
```

---

## 📄 Formato del archivo JSON

Cada archivo `.json` representa un grafo dirigido y ponderado, con el siguiente formato:

```json
{
  "0": [[1, 4], [2, 2]],
  "1": [[2, 5], [3, 10]],
  "2": [[4, 3]],
  "3": [[4, 4]],
  "4": [[5, 1]],
  "5": []
}
```

- Las claves son los identificadores de los nodos (como strings).
- Cada valor es una lista de pares `[vecino, peso]` que representan las aristas salientes.

---
## 📦 Sobre json.hpp
Este proyecto utiliza la biblioteca json.hpp (de nlohmann/json) para manipular archivos .json en C++. Esta biblioteca permite:

Leer archivos .json

Convertir datos JSON a estructuras de C++ (map, vector, etc.)

Escribir archivos JSON desde C++

### 🔧 Cómo se usa en C++
#### C++
#include "json.hpp"

using json = nlohmann::json;

Solo necesitas descargar el archivo json.hpp desde el repositorio oficial y colocarlo en el mismo directorio que tu código C++.
## 📊 Comparación de Rendimiento

| Nodos  | Python (s) | C++ (s) | Diferencia |
|--------|------------|---------|------------|
| 10     | 0.0012     | 0.0004  | C++ es 3x más rápido |
| 100    | 0.0123     | 0.0021  | C++ es 5.8x más rápido |
| 1000   | 0.2751     | 0.0332  | C++ es 8.3x más rápido |
| 10000  | 5.94       | 0.49    | C++ es 12x más rápido |

---

## ✅ Conclusiones

- **Rendimiento:** C++ ejecuta el algoritmo entre 8x y 12x más rápido que Python en grafos grandes. El valor “8.3x” significa que C++ es 8.3 veces más rápido que Python, es decir, que Python demora 8.3 veces más en completar la misma tarea.
- **Memoria:** Python consume entre 7 y 12 veces más memoria que C++, lo cual puede ser un problema en entornos con recursos limitados.
- **Precisión:** Se detectaron pérdidas de precisión en Python al manejar grafos muy grandes (por ejemplo, 5000 nodos o más).
- **Desarrollo:** Python permite escribir el algoritmo y ejecutarlo hasta 3 veces más rápido en tiempo de codificación, ideal para prototipos o educación.

---

## 📚 Referencias

- Cormen, T. H. et al. (2009). *Introducción a los algoritmos*. McGraw-Hill.
- Sedgewick, R. y Wayne, K. (2012). *Algoritmos*. Pearson.
- Knuth, D. (2003). *El arte de programar ordenadores*. Addison-Wesley.
- Dasgupta, S., Papadimitriou, C., Vazirani, U. (2010). *Algoritmos*. McGraw-Hill.

---
