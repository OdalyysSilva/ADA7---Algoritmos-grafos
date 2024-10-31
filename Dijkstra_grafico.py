import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(grafo, inicio):
    distancias = {nodo: float('infinity') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}
    cola_prioridad = [(0, inicio)]
    paso = 0  
    dibujar_paso(grafo, distancias, predecesores, cola_prioridad, inicio, paso)
    paso += 1

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

        dibujar_paso(grafo, distancias, predecesores, cola_prioridad, nodo_actual, paso)
        paso += 1
    
    return distancias, predecesores

def dibujar_grafo_inicial(grafo):
    G = nx.DiGraph()
    
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    
    plt.title("Grafo Inicial")
    plt.show()

def dibujar_paso(grafo, distancias, predecesores, cola_prioridad, nodo_actual, paso):
    G = nx.DiGraph()
    
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    
    nx.draw_networkx_nodes(G, pos, nodelist=[nodo_actual], node_color='orange')
    processed_nodes = [nodo for nodo in distancias if distancias[nodo] < float('infinity') and nodo != nodo_actual]
    nx.draw_networkx_nodes(G, pos, nodelist=processed_nodes, node_color='lightgreen')

    etiquetas_distancias = {nodo: f"{distancias[nodo]:.0f}" if distancias[nodo] < float('infinity') else "∞" for nodo in distancias}
    nx.draw_networkx_labels(G, pos, labels=etiquetas_distancias, font_size=8, font_color='red')
    
    cola_str = ', '.join([f"({nodo}, {dist:.0f})" for dist, nodo in cola_prioridad])
    plt.title(f"Paso {paso}: Nodo actual = {nodo_actual}, Cola = [{cola_str}]")
    plt.show()

def dibujar_grafo_rutas_minimas(grafo, inicio, distancias, predecesores):
    G = nx.DiGraph()
    
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)
    
    for nodo, distancia in distancias.items():
        if predecesores[nodo] is not None:
            nx.draw_networkx_edges(G, pos, edgelist=[(predecesores[nodo], nodo)], width=2, edge_color='red')
    
    plt.title(f"Camino más corto desde {inicio}")
    plt.show()

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

inicio = 'A'

dibujar_grafo_inicial(grafo)
  
distancias, predecesores = dijkstra(grafo, inicio)
print("Distancias mínimas desde el nodo inicial:", distancias)
dibujar_grafo_rutas_minimas(grafo, inicio, distancias, predecesores)
