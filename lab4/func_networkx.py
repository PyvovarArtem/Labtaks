import networkx as nx


def find_path(start, end):
    # Граф - це міста (вершини) і дороги між ними (ребра)
    graph = nx.Graph()
    graph.add_edge("Львів", "Рівне")
    graph.add_edge("Рівне", "Київ")
    graph.add_edge("Київ", "Харків")
    # shortest_path шукає найкоротший шлях
    return nx.shortest_path(graph, start, end)
