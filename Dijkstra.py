import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(grafo, inicio):
    # Inicializamos distancias con infinito para todos los nodos
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}  # Para rastrear la ruta
    # Creamos una cola de prioridad para manejar los nodos y sus distancias
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
    
    return distancias, predecesores

def dibujar_grafo_inicial(grafo):
    G = nx.DiGraph()
    
    # Agregar nodos y aristas al grafo
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)  # Layout del grafo
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    
    plt.title("Grafo Inicial")
    plt.show()

def dibujar_grafo_rutas_minimas(grafo, inicio, distancias, predecesores):
    G = nx.DiGraph()
    
    # Agregar los nodos y aristas al grafo
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)  # Layout del grafo
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    
    # Resaltar el camino mínimo desde el nodo de inicio a cada nodo
    for nodo, distancia in distancias.items():
        if predecesores[nodo] is not None:
            nx.draw_networkx_edges(G, pos, edgelist=[(predecesores[nodo], nodo)], width=2, edge_color='red')
    
    plt.title(f"Camino más corto desde {inicio}")
    plt.show()

# Definir el grafo
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'

# Mostrar el grafo inicial
dibujar_grafo_inicial(grafo)

# Calcular rutas mínimas y mostrar el grafo con rutas resaltadas
distancias, predecesores = dijkstra(grafo, inicio)
print("Distancias mínimas desde el nodo inicial:", distancias)
dibujar_grafo_rutas_minimas(grafo, inicio, distancias, predecesores)
