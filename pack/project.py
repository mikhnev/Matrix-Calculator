import tkinter as tk
import numpy as nm
from pack.SizeChooser import SizeChooser
from pack.Tables import TableResult
from pack.Tables import SimpleTableInput

LARGE_FONT = ("Verdana", 12)


class Calc(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Mult):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(row=0, column=0)

        button = tk.Button(self, text="Multiple",
                           command=lambda: controller.show_frame(Mult))
        button.grid(row=1, column=0)
        '''
        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()'''


class Mult(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A x B", font=LARGE_FONT)
        label.grid(row=0, column=1)

        size_A = label = tk.Label(self, text="Size A", font=LARGE_FONT)
        size_A.grid(row=1, column=0)
        size_B = label = tk.Label(self, text="Size B", font=LARGE_FONT)
        size_B.grid(row=1, column=2)

        self.size_1 = SizeChooser(self)
        self.size_1.grid(row=2, column=0)
        self.size_2 = SizeChooser(self)
        self.size_2.grid(row=2, column=2)

        self.table_1 = SimpleTableInput(self, 2, 2)
        self.table_1.grid(row=4, column=0)
        self.table_2 = SimpleTableInput(self, 2, 2)
        self.table_2.grid(row=4, column=2)

        self.set_1 = tk.Button(self, text="Set", command=lambda: self.update_matrix('A'))
        self.set_1.grid(row=3, column=0)
        self.set_2 = tk.Button(self, text="Set", command=lambda: self.update_matrix('B'))
        self.set_2.grid(row=3, column=2)

        self.result = tk.Button(self, text="Submit", command=self.get_result)
        self.result.grid(row=5, column=1)
        #self.table_r = TableResult(self, self.get_result, self.get_result, self.get_result())
        mult_symbol = tk.Label(self, text="X", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def get_result(self):
        first = []
        for i in range(self.table_1.rows):
            for j in range(self.table_1.columns):
                first.append(self.table_1.get()[i][j])
        m1 = nm.array(first, dtype=float).reshape(self.table_1.rows, self.table_1.columns);
        second = []
        for i in range(self.table_2.rows):
            for j in range(self.table_2.columns):
                second.append(self.table_2.get()[i][j])
        m2 = nm.array(second, dtype=float).reshape(self.table_2.rows, self.table_2.columns);
        result = nm.dot(m1, m2)
        #return result

        self.result = TableResult(self, result.shape[0], result.shape[1], result)
            #SimpleTableInput(self, result.shape[0], result.shape[1])

        self.result.grid(row=5, column=1)
        #self.table_r = TableResult(self, result.shape[0], result.shape[1], result)
        #self.table_r = TableResult(self, result.shape[0], result.shape[1], result)
        # print(result.shape[0])
'''
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


'''

app = Calc()
app.mainloop()
