from tkinter import *
from tkinter import ttk
from functools import partial
from ..database.database import *

FONT = 10
class Table(Frame):
    def __init__(self, master, col_names, table):
        super().__init__(master=master)
        self.cols = col_names
        self.__create(col_names)
        self.name = table

    def __create(self, col_names):
        style = ttk.Style()
        style.configure("mystyle.Treeview.Heading", font=(None, FONT))
        style.configure("mystyle.Treeview", font=(None, FONT))
        scrollbar = Scrollbar(self)
        self.treev = ttk.Treeview(self, columns=col_names, show="headings", yscrollcommand = scrollbar.set, style="mystyle.Treeview")
        self.treev.bind("<<TreeviewSelect>>", self.on_select)
        self.treev.pack(side = LEFT)
        for col in col_names:
            self.treev.heading(column=col, text = col.upper())
            self.treev.column(column=col, width= 110, anchor ='c')

        scrollbar.config(command = self.treev.yview )
        scrollbar.pack(side = LEFT, fill = Y )



    def on_select(self, event):
        self.select_item = self.treev.selection()[-1]
        self.select_values = self.treev.item(self.select_item)['values']
        

    def append_data(self, data, tags):
        self.treev.insert('', END, values=data, tags=tags)

    def add_list_data(self, colnames, list_data):
        self.tags = [('odd',) , ('even',)]
        for data in list_data:
            values = [data[col] for col in colnames]
            self.append_data(values, self.tags[0])
            self.tags.reverse()

        self.treev.tag_configure('odd', background='#E8E8E8')
        self.treev.tag_configure('even', background='#FFFFFF')

    def insert_data(self, colnames, data):
        values = [data[col] for col in colnames]
        self.append_data(values, self.tags[0])
        self.tags.reverse()
        self.treev.tag_configure('odd', background='#E8E8E8')
        self.treev.tag_configure('even', background='#FFFFFF')
        

# if __name__ == "__main__":
#     win = Tk("NOPE")
#     colnames, result = get_animals()
#     table = Table(win, colnames)
#     table.add_list_data(colnames, result)
#     table.pack(Fill = BOTH, expand = True)
#     win.mainloop()