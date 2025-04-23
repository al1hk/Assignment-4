import tkinter as tk

class EraserCanvas:
    def __init__(self, root, width, height, cell_size):
        self.root = root
        self.canvas = tk.Canvas(root, width=width, height=height, bg="white")
        self.canvas.pack()

        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.cells = []

        self.create_grid()
        self.eraser = None
        self.eraser_size = cell_size  # Size of the eraser
        self.eraser_rect = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, outline="red", width=2)

        self.canvas.bind("<B1-Motion>", self.move_eraser)
        self.canvas.bind("<ButtonRelease-1>", self.eraser_stop)

    def create_grid(self):
        """ Create the grid of blue cells. """
        for i in range(0, self.width, self.cell_size):
            row = []
            for j in range(0, self.height, self.cell_size):
                cell = self.canvas.create_rectangle(i, j, i + self.cell_size, j + self.cell_size, fill="blue", outline="blue")
                row.append(cell)
            self.cells.append(row)

    def move_eraser(self, event):
        """ Move the eraser around the canvas. """
        x, y = event.x, event.y
        # Calculate the top-left corner of the eraser
        x1 = (x // self.cell_size) * self.cell_size
        y1 = (y // self.cell_size) * self.cell_size
        x2 = x1 + self.eraser_size
        y2 = y1 + self.eraser_size

        # Move the eraser
        self.canvas.coords(self.eraser_rect, x1, y1, x2, y2)

        # Erase cells within the bounds of the eraser
        self.erase_cells(x1, y1, x2, y2)

    def erase_cells(self, x1, y1, x2, y2):
        """ Erase cells that intersect with the eraser. """
        for row in self.cells:
            for cell in row:
                cell_coords = self.canvas.coords(cell)
                # Check if the cell intersects with the eraser
                if not (cell_coords[2] < x1 or cell_coords[0] > x2 or cell_coords[3] < y1 or cell_coords[1] > y2):
                    self.canvas.itemconfig(cell, fill="white")  # Change cell color to white

    def eraser_stop(self, event):
        """ Stop erasing when mouse button is released. """
        self.eraser = None

def main():
    root = tk.Tk()
    root.title("Eraser on Canvas")

    canvas_width = 600
    canvas_height = 400
    cell_size = 20

    eraser_app = EraserCanvas(root, canvas_width, canvas_height, cell_size)
    
    root.mainloop()

if __name__ == "__main__":
    main()
