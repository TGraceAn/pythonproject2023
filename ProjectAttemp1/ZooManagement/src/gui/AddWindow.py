from tkinter import *
from functools import partial
from tkinter.ttk import Treeview
from .Table import Table

class AddWindow(Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.data_update = []

    def add_widget(self, row_names: list[str], padx=4, pady=2):
        frame = Frame(self)
        frame.pack(side=TOP)

        self.entrys = []
        for index_row in range(0, len(row_names)):
            label = Label(frame, text=row_names[index_row].upper())
            label.pack()
            entry = Entry(frame)
            entry.pack()
            self.entrys.append(entry)
        self.submit = Button(self, text = "Submit")
        self.submit.pack(padx = padx, pady = pady)
        self.submit.config(command=partial(self.add_submit_handle))

    def change2repair(self):
        self.submit.config(command=partial(self.repair_submit_handle))

    def insert_data(self, values):
        for index in range(0, len(self.entrys)):
            self.entrys[index].insert(0, str(values[index]))

    def add_submit_handle(self):
        data = self.get_entry_data()
        cols = self.table.cols

        list_data = {}
        for index in range(0, len(cols)):
            list_data.update({cols[index] : data[index]})
        self.data_update.append(list_data)
        try:
            self.table.insert_data(self.table.cols, list_data)
        except:
            pass
        self.alert.config(text=f"Submit {data[0]} success")

    def set_alert(self, alert):
        self.alert = alert

    def repair_submit_handle(self):
            data = self.get_entry_data()
            cols = self.table.cols
            item = self.table.select_item
            self.table.treev.item(item, values=data)

            list_data = {}
            for index in range(0, len(cols)):
                list_data.update({cols[index] : data[index]})
            self.data_update.append(list_data)


    def get_entry_data(self):
        data_list = []
        for entry in self.entrys:
            data_list.append(entry.get())

        return data_list
    
    def set_table(self, table : Table):
        self.table = table


if __name__ == "__main__":
    win = AddWindow("NOPE")

    win.mainloop()