def encontrar_todos_los_caminos(grafo, nodo_actual, destino, camino_actual, tiempo_actual, todos_los_caminos):
    # Agregamos el nodo actual a la ruta que estamos construyendo
    camino_actual.append(nodo_actual)
    
    # Si llegamos al destino, guardamos esta ruta con su tiempo acumulado
    if nodo_actual == destino:
        todos_los_caminos.append((list(camino_actual), tiempo_actual))
    else:
        # Exploramos TODOS los vecinos disponibles de manera exhaustiva
        for vecino, peso in grafo[nodo_actual].items():
            if vecino not in camino_actual:  # Evita regresar por donde ya pasamos
                encontrar_todos_los_caminos(
                    grafo, vecino, destino, camino_actual, tiempo_actual + peso, todos_los_caminos
                )
                
    # Deshacemos el último paso para que el algoritmo pueda evaluar otras combinaciones
    camino_actual.pop()

def resolver_fuerza_bruta(grafo, inicio, fin):
    todos_los_caminos = []
    encontrar_todos_los_caminos(grafo, inicio, fin, [], 0, todos_los_caminos)
    
    print(f"--- RUTAS ENCONTRADAS POR FUERZA BRUTA ({len(todos_los_caminos)} en total) ---")
    for r, t in todos_los_caminos:
        print(f"Ruta: {' -> '.join(r)} | Tiempo: {t} minutos")
    print("-" * 50)
    
    # Buscamos la combinación que tenga el menor tiempo acumulado
    ruta_optima, tiempo_minimo = min(todos_los_caminos, key=lambda x: x[1])
    return tiempo_minimo, ruta_optima

# Definición del grafo basado en la imagen del ejercicio
grafo_carreteras = {
    'A': {'B': 90, 'C': 138, 'D': 348},
    'B': {'C': 66, 'E': 82},
    'C': {'D': 156, 'F': 90},
    'D': {'G': 48},
    'E': {'F': 120, 'I': 82},
    'F': {'H': 60, 'G': 130},
    'G': {'H': 48, 'J': 148},
    'H': {'I': 130, 'J': 124},
    'I': {'J': 124},
    'J': {}
}

# Ejecución
origen = 'A'
destino = 'J'
tiempo_total, camino_optimo = resolver_fuerza_bruta(grafo_carreteras, origen, destino)

print("--- GANADOR POR FUERZA BRUTA ---")
print(f"Ruta óptima mínima: {' -> '.join(camino_optimo)}")
print(f"Tiempo mínimo total de manejo: {tiempo_total} minutos")