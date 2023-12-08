from app import App
import tkinter as tk
from apath import get_asset_path

def main():
    map_path = get_asset_path("map.png")
    graph_nodes_path = get_asset_path("graph.txt")
    
    point_list = []

    def on_mouse_pressed(event: tk.Event, canvas: tk.Canvas):
        x, y = event.x, event.y
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

        x_norm = x / canvas.winfo_width()
        y_norm = y / canvas.winfo_height()
        point_list.append((x_norm, y_norm))

    app = App("Map", 500, map_path)
    app.on_click(on_mouse_pressed)
    app.run()

    print(point_list)
    with open(graph_nodes_path, "w") as f:
        for i, (x, y) in enumerate(point_list):
            f.write(f"{i + 1} {x} {y}\n")


if __name__ == "__main__":
    main()