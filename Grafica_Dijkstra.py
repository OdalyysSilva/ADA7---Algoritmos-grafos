import heapq

def dijkstra(grafo, inicio):
    # Inicializamos distancias con infinito para todos los nodos
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    # Creamos una cola de prioridad para manejar los nodos y sus distancias
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Verificamos si la distancia actual es mayor a la registrada (puede suceder en algunos casos)
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Revisamos los nodos vecinos y calculamos la distancia
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            # Si la distancia es menor, actualizamos la distancia y añadimos a la cola
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'
distancias = dijkstra(grafo, inicio)
print("Distancias mínimas desde el nodo inicial:", distancias)
