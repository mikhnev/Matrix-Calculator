import tkinter as tk


def update_matrix(self, matrix):
    if matrix == 'A':
        self.table_1.destroy()
        self.table_1 = SimpleTableInput(self, int(self.size_1.rows.get()), int(self.size_1.columns.get()))
        self.table_1.grid(row=4, column=0)
    else:
        self.table_2.destroy()
        self.table_2 = SimpleTableInput(self, int(self.size_2.rows.get()), int(self.size_2.columns.get()))
        self.table_2.grid(row=4, column=2)


class TableResult(tk.Frame):
    def __init__(self, parent, rows, columns, result):
        tk.Frame.__init__(self, parent)
        self.rows = rows
        self.columns = columns
        self._entry = {}
        #vcmd = (self.register(self._validate), "%P")
        for r in range(self.rows):
            for c in range(self.columns):
                index = (r, c)
                e = tk.Entry(self, validate="key")
                e.grid(row=r, column=c, stick="nsew")
                e.insert(0, result[r][c])
                self._entry[index] = e

class SimpleTableInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self._entry = {}
        self.rows = rows
        self.columns = columns
        # register a command to use for validation
        vcmd = (self.register(self._validate), "%P")
        # create the table of widgets
        for row in range(self.rows):
            for column in range(self.columns):
                index = (row, column)
                e = tk.Entry(self, validate="key", validatecommand=vcmd)
                e.grid(row=row, column=column, stick="nsew")
                self._entry[index] = e
        # adjust column weights so they all expand equally
        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)
        # designate a final, empty row to fill up any extra space
        self.grid_rowconfigure(rows, weight=1)

    def get(self):
        '''Return a list of lists, containing the data in the table'''
        result = []
        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                index = (row, column)
                current_row.append(self._entry[index].get())
            result.append(current_row)
        return result

    def _validate(self, P):
        '''Perform input validation.

        Allow only an empty value, or a value that can be converted to a float
        '''
        if P.strip() == "":
            return True

        try:
            f = float(P)
        except ValueError:
            self.bell()
            return False
        return True


