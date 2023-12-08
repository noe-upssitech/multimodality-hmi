import tkinter as tk
import network
from PIL import Image, ImageTk
from dataclasses import dataclass
from modal.vocal import Vocal

class App:

    @dataclass
    class Node:
        id: int
        handle: int

    root: tk.Tk
    canvas: tk.Canvas

    def __init__(self, name: str, size: int, path_to_map: str, path_to_graph: str):
        self.root = tk.Tk()
        self.root.title(name)
        self.root.geometry(f"{size}x{size}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(self.root, width=size, height=size)
        self.canvas.pack()

        self.set_map_as_bg(path_to_map)
        self.graph = network.create_graph(path_to_graph, size)

        self.start_node: self.Node = None
        self.end_node: self.Node = None
        self.lines = []

        self.configure_click()



    def set_map_as_bg(self, path_to_map: str):
        """Sets the map as the background of the canvas"""
        self.root.update_idletasks()

        image = Image.open(path_to_map)
        image = image.resize((self.root.winfo_width(), self.root.winfo_height()), Image.LANCZOS)
        tk_image = ImageTk.PhotoImage(image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        self.canvas.image = tk_image



    def update(self, var_name, id):
        cur_node: self.Node = getattr(self, var_name)
        if cur_node is not None:
            self.canvas.delete(cur_node.handle)

        for line_handle in self.lines:
            self.canvas.delete(line_handle)
        self.lines = []

        if id is None or not self.graph.has_node(id):
            setattr(self, var_name, None)
            return

        x, y = self.graph.nodes[id]["pos"]
        r = 10

        handle = self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
        setattr(self, var_name, self.Node(id, handle))            

        print(f"{self.start_node=} {self.end_node=}")
        if self.start_node is not None and self.end_node is not None:
            path = self.graph.compute_shortest_path(self.start_node.id, self.end_node.id)
            for i in range(len(path) - 1):
                x1, y1 = self.graph.nodes[path[i]]["pos"]
                x2, y2 = self.graph.nodes[path[i + 1]]["pos"]

                self.lines.append(self.canvas.create_line(x1, y1, x2, y2, fill="red", width=4))



    def configure_click(self):
        def on_click(event):
            x, y = event.x, event.y
            self.update("end_node", None)

            # Find the closest node to the click
            closest_node = None
            closest_dist = float("inf")
            for node in self.graph.nodes:
                node_x, node_y = self.graph.nodes[node]["pos"]
                dist = (node_x - x) ** 2 + (node_y - y) ** 2
                if dist < closest_dist:
                    closest_node = node
                    closest_dist = dist

            self.update("start_node", closest_node)
            id = self.vocal.interpret(self.vocal.listen())
            if id is not None:
                self.update("end_node", id)

        self.canvas.bind("<Button-1>", on_click)
        self.canvas.bind("<Button-3>", lambda e: self.update("start_node", None))


    def set_vocal(self, vocal):
        self.vocal: Vocal = vocal



    def run(self):
        self.root.mainloop()


