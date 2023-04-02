from tkinter import *
from .Table import Table

class AddWindow(Tk):
    def __init__(self, title, repair):
        super().__init__()
        self.title(title)
        self.data_update = {}
        self.__repair = repair

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
        if self.__repair == True:
            self.submit = Button(self, text = "Submit", command=self.repair_submit_handle)
        else:
            self.submit = Button(self, text = "Submit", command=self.add_submit_handle)
        self.submit.pack(padx = padx, pady = pady)

    def insert_data(self, values):
        for index in range(0, len(self.entrys)):
            self.entrys[index].insert(0, str(values[index]))

    def add_submit_handle(self):
        data = self.get_entry_data()
        cols = self.table.cols

        list_data = {}
        for index in range(0, len(cols)):
            self.data_update.update({cols[index] : data[index]})
            list_data.update({cols[index] : data[index]})
        try:
            self.table.insert_data(self.table.cols, list_data)
        except:
            pass
        self.alert.config(text=f"Submit {data[0]} success")
        self.destroy()

    def set_alert(self, alert):
        self.alert = alert

    def repair_submit_handle(self):
        data = self.get_entry_data()
        cols = self.table.cols
        item = self.table.select_item
        self.table.treev.item(item, values=data)
        for index in range(0, len(cols)):
            self.data_update.update({cols[index] : data[index]})
        self.destroy()

    def get_data_list(self):
        return self.data_update

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
    