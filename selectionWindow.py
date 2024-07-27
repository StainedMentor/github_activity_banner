

import tkinter as tk

class CheckboxGrid(tk.Frame):
    def __init__(self, parent, rows, cols):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.grid_values = [[0 for _ in range(cols)] for _ in range(rows)]


        for r in range(rows):
            for c in range(cols):
                var = tk.IntVar(value=self.grid_values[r][c])
                cb = tk.Checkbutton(self, variable=var, command=lambda r=r, c=c, var=var: self.update_value(r, c, var))
                cb.grid(row=r, column=c)


    def update_value(self, row, col, var):
        self.grid_values[row][col] = var.get()


    def print_grid(self):
        for row in self.grid_values:
            print(''.join('■' if cell == 1 else ' ' for cell in row))


