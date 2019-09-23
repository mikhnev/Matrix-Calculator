import tkinter as tk

LARGE_FONT = ("Verdana", 12)
class SizeChooser(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.rows = tk.Entry(self)
        self.rows.grid(row=0, column=0)
        label = tk.Label(self, text=" x ", font=LARGE_FONT)
        label.grid(row=0, column=1)
        self.columns = tk.Entry(self)
        self.columns.grid(row=0, column=2)

