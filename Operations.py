import tkinter as tk
import numpy as nm
from SizeChooser import *
from Tables import *
from Simple_operations import *

LARGE_FONT = ("Verdana", 12)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.grid(row=0, column=0)

        button = tk.Button(self, text="Multiple",
                           command=lambda: controller.show_frame(Mult))
        button.grid(row=1, column=0)
        button = tk.Button(self, text="Summarize",
                           command=lambda: controller.show_frame(Sum))
        button.grid(row=1, column=1)
        button = tk.Button(self, text="Subtraction",
                           command=lambda: controller.show_frame(Subtract))
        button.grid(row=1, column=2)
        button = tk.Button(self, text="Transpose",
                           command=lambda: controller.show_frame(Transpose))
        button.grid(row=1, column=3)
        button = tk.Button(self, text="Determinant",
                           command=lambda: controller.show_frame(Determinant))
        button.grid(row=2, column=0)
        button = tk.Button(self, text="Inverse",
                           command=lambda: controller.show_frame(Inverse))
        button.grid(row=2, column=1)
        button = tk.Button(self, text="Power",
                           command=lambda: controller.show_frame(Power))
        button.grid(row=2, column=2)

class Determinant(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A (Det)", font=LARGE_FONT)
        label.grid(row=0, column=1)

        size_A = label = tk.Label(self, text="Size A", font=LARGE_FONT)
        size_A.grid(row=1, column=0)
        self.size_1 = SizeChooser(self)
        self.size_1.grid(row=2, column=0)

        self.table_1 = SimpleTableInput(self, 2, 2)
        self.table_1.grid(row=4, column=0)
        self.set_1 = tk.Button(self, text="Set", command=lambda: self.update_matrix('A'))
        self.set_1.grid(row=3, column=0)

        self.result = tk.Button(self, text="Determinant", command=self.get_result)
        self.result.grid(row=5, column=1)
        mult_symbol = tk.Label(self, text="", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

    def get_result(self):
        first = []
        for i in range(self.table_1.rows):
            for j in range(self.table_1.columns):
                first.append(self.table_1.get()[i][j])
        m1 = nm.array(first, dtype=float).reshape(self.table_1.rows, self.table_1.columns);
        result =  (do_det(m1))
        print (result)
        self.result = NumberResult(self, result)
        self.result.grid(row=5, column=1)


class Transpose(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A (Tr)", font=LARGE_FONT)
        label.grid(row=0, column=1)

        size_A = label = tk.Label(self, text="Size A", font=LARGE_FONT)
        size_A.grid(row=1, column=0)
        self.size_1 = SizeChooser(self)
        self.size_1.grid(row=2, column=0)

        self.table_1 = SimpleTableInput(self, 2, 2)
        self.table_1.grid(row=4, column=0)
        self.set_1 = tk.Button(self, text="Set", command=lambda: self.update_matrix('A'))
        self.set_1.grid(row=3, column=0)

        self.result = tk.Button(self, text="Transpose", command=self.get_result)
        self.result.grid(row=5, column=1)
        mult_symbol = tk.Label(self, text="", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

    def get_result(self):
        first = []
        for i in range(self.table_1.rows):
            for j in range(self.table_1.columns):
                first.append(self.table_1.get()[i][j])
        m1 = nm.array(first, dtype=float).reshape(self.table_1.rows, self.table_1.columns);
        result =  (do_transpose(m1))
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)


class Inverse(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A (Inv)", font=LARGE_FONT)
        label.grid(row=0, column=1)

        size_A = label = tk.Label(self, text="Size A", font=LARGE_FONT)
        size_A.grid(row=1, column=0)
        self.size_1 = SizeChooser(self)
        self.size_1.grid(row=2, column=0)

        self.table_1 = SimpleTableInput(self, 2, 2)
        self.table_1.grid(row=4, column=0)
        self.set_1 = tk.Button(self, text="Set", command=lambda: self.update_matrix('A'))
        self.set_1.grid(row=3, column=0)

        self.result = tk.Button(self, text="Inverse", command=self.get_result)
        self.result.grid(row=5, column=1)
        mult_symbol = tk.Label(self, text="", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

    def get_result(self):
        first = []
        for i in range(self.table_1.rows):
            for j in range(self.table_1.columns):
                first.append(self.table_1.get()[i][j])
        m1 = nm.array(first, dtype=float).reshape(self.table_1.rows, self.table_1.columns);
        result =  (do_inv(m1))
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)


class Power(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A (Pow)", font=LARGE_FONT)
        label.grid(row=0, column=1)

        size_A = label = tk.Label(self, text="Size A", font=LARGE_FONT)
        size_A.grid(row=1, column=0)
        self.size_1 = SizeChooser(self)
        self.size_1.grid(row=2, column=0)

        self.table_1 = SimpleTableInput(self, 2, 2)
        self.table_1.grid(row=4, column=0)
        self.set_1 = tk.Button(self, text="Set", command=lambda: self.update_matrix('A'))
        self.set_1.grid(row=3, column=0)

        self.power_label = tk.Label(self, text="Power", font=LARGE_FONT)
        self.power_label.grid(row=1, column=1)
        self.npow = tk.Entry(self)
        self.npow.grid(row=2, column=1)
        self.set_2 = tk.Button(self, text="Set", command=self.get_pow)
        self.set_2.grid(row=3, column=1)

        self.result = tk.Button(self, text="Power", command=self.get_result)
        self.result.grid(row=6, column=1)
        

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=7, column=1)

    def get_pow(self):
        self.n = int(self.npow.get())

    def get_result(self):
        first = []
        for i in range(self.table_1.rows):
            for j in range(self.table_1.columns):
                first.append(self.table_1.get()[i][j])
        m1 = nm.array(first, dtype=float).reshape(self.table_1.rows, self.table_1.columns);
        result =  (do_pow(m1, self.n))
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)


class Subtract(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A - B", font=LARGE_FONT)
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
        mult_symbol = tk.Label(self, text="-", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

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
        result =  (do_subtract(m1, m2))
        #result = nm.dot(m1, m2)
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)


class Sum(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="A + B", font=LARGE_FONT)
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
        mult_symbol = tk.Label(self, text="+", font=LARGE_FONT)
        mult_symbol.grid(row=4, column=1)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=6, column=1)

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
        result =  (do_sum(m1, m2))
        #result = nm.dot(m1, m2)
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)



class Mult(tk.Frame):

    def update_matrix(self, matrix):
        if matrix == 'A':
            self.table_1.destroy()
            self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
            self.table_1.grid(row=4, column=0)
        else:
            self.table_2.destroy()
            self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
            self.table_2.grid(row=4, column=2)

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
        result =  (do_mult(m1, m2))
        #result = nm.dot(m1, m2)
        self.result = TableResult(self, result.shape[0], result.shape[1], result)
        self.result.grid(row=5, column=1)
