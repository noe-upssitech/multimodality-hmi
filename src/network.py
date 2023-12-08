from apath import get_asset_path
import networkx as nx
import matplotlib.pyplot as plt

def create_graph(path_to_graph, window_size):
    graph = nx.Graph()

    with open(path_to_graph, "r") as f:
        nodes_str, edges_str = [s.strip().split("\n") for s in f.read().split("\n\n")]
        
        def create_node(line):
            node_id, x, y = map(float, line.split())
            return (int(node_id), {"pos": (x * window_size, y * window_size)})

        graph_nodes = [create_node(line) for line in nodes_str if line != ""]
        graph_edges = [tuple(map(int, line.split())) for line in edges_str if line != ""]
    
    graph.add_nodes_from(graph_nodes)
    graph.add_edges_from(graph_edges)

    graph.compute_shortest_path = lambda start, end: nx.astar_path(graph, start, end)

    return graph

if __name__ == "__main__":
    G = create_graph(get_asset_path("city.graph"), 500)

    print(nx.astar_path(G, 1, 30))

    pos = nx.get_node_attributes(G, 'pos')
    flipped_pos = {node: (x,-y) for (node, (x,y)) in pos.items()}

    nx.draw(G, flipped_pos, with_labels=True, font_weight='bold')
    plt.show()  