from apath import get_asset_path
from app import App
import tkinter as tk

def main():
    map_path = get_asset_path("map.png")
    graph_nodes_path = get_asset_path("city.graph")

    # Load the graph data
    with open(graph_nodes_path, "r") as f:
        nodes_str, edges_str = [s.strip().split("\n") for s in f.read().split("\n\n")]
        
        graph_nodes = [tuple(map(float, line.split())) for line in nodes_str if line != ""]
        graph_edges = [tuple(map(int, line.split())) for line in edges_str if line != ""]
        print(graph_edges)

    app = App("Map", 500, map_path, graph_nodes_path)

    def fit_coords(x: float, y: float):
        return (int(x * app.root.winfo_width()), int(y * app.root.winfo_height()))

    app.root.update_idletasks()

    # Draw the edges
    for (i, j) in graph_edges:
        x1, y1 = fit_coords(graph_nodes[i - 1][1], graph_nodes[i - 1][2])
        x2, y2 = fit_coords(graph_nodes[j - 1][1], graph_nodes[j - 1][2])

        app.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

    # Draw the nodes
    for (i, x, y) in graph_nodes:
        x, y = fit_coords(x, y) 

        r = 10
        app.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
        app.canvas.create_text(x, y, text=str(int(i)))
    

    app.run()


if __name__ == "__main__":
    main()