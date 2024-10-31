import networkx as nx
import matplotlib.pyplot as plt

class UnionFind:
    def __init__(self, elementos):
        self.padre = {elemento: elemento for elemento in elementos}
        self.rango = {elemento: 0 for elemento in elementos}

    def encontrar(self, u):
        if self.padre[u] != u:
            self.padre[u] = self.encontrar(self.padre[u])
        return self.padre[u]

    def unir(self, u, v):
        raiz_u = self.encontrar(u)
        raiz_v = self.encontrar(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1

def kruskal(grafo):
    aristas = []
    for u in grafo:
        for v, peso in grafo[u]:
            if (peso, v, u) not in aristas:
                aristas.append((peso, u, v))
    aristas.sort()
    uf = UnionFind(grafo.keys())
    agm = []
    for peso, u, v in aristas:
        if uf.encontrar(u) != uf.encontrar(v):
            uf.unir(u, v)
            agm.append((u, v, peso))
    return agm

def dibujar_agm(agm, nombre_grafo="Árbol Generador Mínimo"):
    grafo_agm = nx.Graph()
    for u, v, peso in agm:
        grafo_agm.add_edge(u, v, weight=peso)

    pos = nx.spring_layout(grafo_agm)
    nx.draw(grafo_agm, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=10)
    labels = nx.get_edge_attributes(grafo_agm, 'weight')
    nx.draw_networkx_edge_labels(grafo_agm, pos, edge_labels=labels)
    plt.title(nombre_grafo)
    plt.show()

# Ejemplo 1
ciudades = {
    'San Francisco': [('Denver', 900), ('Chicago', 1200), ('Nueva York', 2000), ('Atlanta', 2200)],
    'Denver': [('San Francisco', 900), ('Chicago', 1300), ('Nueva York', 1600), ('Atlanta', 1400)],
    'Chicago': [('San Francisco', 1200), ('Denver', 1300), ('Nueva York', 1000), ('Atlanta', 700)],
    'Nueva York': [('San Francisco', 2000), ('Denver', 1600), ('Chicago', 1000), ('Atlanta', 800)],
    'Atlanta': [('San Francisco', 2200), ('Denver', 1400), ('Chicago', 700), ('Nueva York', 800)]
}

# Ejemplo 2
grafo = {
    'a': [('b', 2), ('e', 3)],
    'b': [('a', 2), ('c', 3), ('f', 1)],
    'c': [('b', 3), ('d', 1), ('g', 2)],
    'd': [('c', 1), ('h', 5)],
    'e': [('a', 3), ('f', 4), ('i', 4)],
    'f': [('b', 1), ('e', 4), ('g', 3), ('j', 2)],
    'g': [('c', 2), ('f', 3), ('h', 3), ('k', 4)],
    'h': [('d', 5), ('g', 3), ('l', 3)],
    'i': [('e', 4), ('j', 3)],
    'j': [('f', 2), ('i', 3), ('k', 3)],
    'k': [('g', 4), ('j', 3), ('l', 1)],
    'l': [('h', 3), ('k', 1)],
}

# Encontrar el AGM y desplegarlo
agm_ciudades = kruskal(ciudades)
print("Componentes del Árbol de Expansión Mínima (Ejemplo 1):")
for u, v, peso in agm_ciudades:
    print(f"{u} - {v}: {peso}")
dibujar_agm(agm_ciudades, "Árbol Generador Mínimo - Ciudades")

agm_grafo = kruskal(grafo)
print("\nComponentes del Árbol de Expansión Mínima (Ejemplo 2):")
for u, v, peso in agm_grafo:
    print(f"{u} - {v}: {peso}")
dibujar_agm(agm_grafo, "Árbol Generador Mínimo - Grafo")
