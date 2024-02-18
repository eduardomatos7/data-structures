import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def extrair_min(Q):
    min_idx = 0

    for i in range(1, len(Q)):
        if Q[i][0] < Q[min_idx][0]:
            min_idx = i

    return Q.pop(min_idx)

def prim(G, inicio):
    π = {v: None for v in G}
    Q = [(0, inicio, None)]
    S = set()

    G_visual = nx.Graph()  # Visualização do grafo função

    while Q:
        peso, v, pai = extrair_min(Q)

        if v not in S:
            S.add(v)

            if pai is not None:
                print(f"{pai} -> {v} {peso}")
                G_visual.add_edge(pai, v, weight=peso)

            if v in G:
                for u, peso_uv in G[v].items():
                    if u not in S and (π[u] is None or peso_uv < G[v][π[u]]):
                        Q.append((peso_uv, u, v))
                        π[u] = v

    # funções para ver o grafo
    pos = nx.spring_layout(G_visual)
    labels = nx.get_edge_attributes(G_visual, 'weight')
    nx.draw(G_visual, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(G_visual, pos, edge_labels=labels)
    plt.show()

# Ler dados da planilha
df = pd.read_excel('distancias.xlsx')

# Criar o grafo a partir dos dados da planilha
grafo = {}
for index, row in df.iterrows():
    origem = row['Origem']
    destino = row['Destino']
    distancia = row['Distancia']

    if origem not in grafo:
        grafo[origem] = {}

    if destino not in grafo:
        grafo[destino] = {}

    grafo[origem][destino] = distancia
    grafo[destino][origem] = distancia  # Grafo não-direcionado

# Mostrar cidades no grafo
print("Cidades no grafo:", list(grafo.keys()))

vertice_inicio = input("Vértice inicial: ")
prim(grafo, vertice_inicio)
