import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import tkinter as tk
from tkinter import ttk

def extrair_min(Q):
    min_idx = 0

    for i in range(1, len(Q)):
        if Q[i][0] < Q[min_idx][0]:
            min_idx = i

    return Q.pop(min_idx)

def prim_animation(G, inicio, entry_pesos):
    π = {v: None for v in G}
    Q = [(0, inicio, None)]
    S = set()

    fig, ax = plt.subplots(figsize=(8, 8))
    G_visual = nx.Graph()

    def update(frame):
        nonlocal G_visual
        nonlocal S

        if Q:
            peso, v, pai = extrair_min(Q)

            if v not in S:
                S.add(v)

                if pai is not None:
                    G_visual.add_edge(pai, v, weight=peso, color='blue', font_size=5)
                    entry_pesos.insert(tk.END, f"{pai} -> {v} {peso}\n")

                if v in G:
                    for u, peso_uv in G[v].items():
                        if u not in S and (π[u] is None or peso_uv < G[v][π[u]]):
                            Q.append((peso_uv, u, v))
                            π[u] = v

            pos = nx.spring_layout(G_visual, seed=43, k=1.5)
            labels = nx.get_edge_attributes(G_visual, 'weight')
            node_colors = ['blue' if node == inicio else 'red' if node == v else 'lightblue' for node in G_visual.nodes()]
            edge_colors = ['blue' if (u, v) in G_visual.edges(data=False) and (v, u) in G_visual.edges(data=False) else 'gray'
                           for u, v in G_visual.edges()]

            ax.clear()
            nx.draw(G_visual, pos, with_labels=True, font_weight='bold', node_color=node_colors, edge_color='black',
                    node_size=400, font_size=6)
            nx.draw_networkx_edge_labels(G_visual, pos, edge_labels=labels, font_size=8)

    ani = FuncAnimation(fig, update, frames=range(len(G)), interval=400)

    return fig, ani

def iniciar_animacao(grafo):
    def iniciar_animacao_callback():
        vertice_inicio = combo_cidades.get()
        fig, ani = prim_animation(grafo, vertice_inicio, entry_pesos)

        window_animacao = tk.Toplevel(root)
        window_animacao.title("Grafo")
        window_animacao.geometry("800x600")

        canvas = FigureCanvasTkAgg(fig, master=window_animacao)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        ani.event_source.start()
        window_animacao.protocol("WM_DELETE_WINDOW", lambda: on_closing(window_animacao, ani))

    root = tk.Tk()
    root.title("Seleção de Cidade Inicial")
    root.geometry("400x300")

    frame = ttk.Frame(root)
    frame.pack(expand=True, pady=20)

    label_cidade = ttk.Label(frame, text="Selecione a Cidade Inicial:")
    label_cidade.pack(pady=10)

    cidades = list(grafo.keys())

    combo_cidades = ttk.Combobox(frame, values=cidades)
    combo_cidades.set(cidades[0])
    combo_cidades.pack(pady=10)

    btn_iniciar_animacao = ttk.Button(frame, text="Iniciar", command=iniciar_animacao_callback)
    btn_iniciar_animacao.pack()

    entry_pesos = tk.Text(root, width=30, height=15)
    entry_pesos.pack(pady=10)

    def on_closing(window, animation):
        plt.close(animation._fig)
        window.destroy()

    root.mainloop()

# Ler os  dados da planilha
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
    grafo[destino][origem] = distancia

iniciar_animacao(grafo)
