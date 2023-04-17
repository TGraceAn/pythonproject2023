from tkinter import *
from .Table import Table
def on_focus_in(entry):
    entry.delete(0,"end")

def on_focus_out(entry, placeholder):
    if entry.get() == "":
        entry.insert(0, placeholder)

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
            if row_names[index_row] == "DOB":
                entry_dob = Entry(frame)
                entry_dob.pack()
                entry_dob.insert(0,"yyyy-mm-dd")
                entry_dob.bind('<FocusOut>', lambda x: on_focus_out(entry_dob, "yyyy-mm-dd"))
                entry_dob.bind('<FocusIn>', lambda x: on_focus_in(entry_dob))
                self.entrys.append(entry_dob)
            elif row_names[index_row].upper() == "PHONENUMBER":
                entry_pn = Entry(frame)
                entry_pn.pack()
                entry_pn.insert(0,"0xxxxxxxxx")
                entry_pn.bind('<FocusOut>', lambda x: on_focus_out(entry_pn, "0xxxxxxxxx"))
                entry_pn.bind('<FocusIn>', lambda x: on_focus_in(entry_pn))
                self.entrys.append(entry_pn)
            elif row_names[index_row].upper() == "ANIMALID":
                entry_aid = Entry(frame)
                entry_aid.pack()
                entry_aid.insert(0,"XXXXXXXXX")
                entry_aid.bind('<FocusOut>', lambda x: on_focus_out(entry_aid, "XXXXXXXXX"))
                entry_aid.bind('<FocusIn>', lambda x: on_focus_in(entry_aid))
                self.entrys.append(entry_aid)
            elif row_names[index_row].upper() == "SPECIES":
                entry_as = Entry(frame)
                entry_as.pack()
                entry_as.insert(0,"Enter species name")
                entry_as.bind('<FocusOut>', lambda x: on_focus_out(entry_as, "Enter species name"))
                entry_as.bind('<FocusIn>', lambda x: on_focus_in(entry_as))
                self.entrys.append(entry_as)
            elif row_names[index_row].upper() == "DATEOFBIRTH":
                entry_adob = Entry(frame)
                entry_adob.pack()
                entry_adob.insert(0,"yyyy-mm-dd")
                entry_adob.bind('<FocusOut>', lambda x: on_focus_out(entry_adob, "yyyy-mm-dd"))
                entry_adob.bind('<FocusIn>', lambda x: on_focus_in(entry_adob))
                self.entrys.append(entry_adob)
            elif row_names[index_row].upper() == "DATEOFADMISSION":
                entry_adoa = Entry(frame)
                entry_adoa.pack()
                entry_adoa.insert(0,"yyyy-mm-dd")
                entry_adoa.bind('<FocusOut>', lambda x: on_focus_out(entry_adoa, "yyyy-mm-dd"))
                entry_adoa.bind('<FocusIn>', lambda x: on_focus_in(entry_adoa))
                self.entrys.append(entry_adoa)
            elif row_names[index_row].upper() == "EMPLOYEEID":
                entry_eid = Entry(frame)
                entry_eid.pack()
                entry_eid.insert(0,"XX*******")
                entry_eid.bind('<FocusOut>', lambda x: on_focus_out(entry_eid, "XX*******"))
                entry_eid.bind('<FocusIn>', lambda x: on_focus_in(entry_eid))
                self.entrys.append(entry_eid)
            elif row_names[index_row].upper() == "STAFFID":
                entry_sid = Entry(frame)
                entry_sid.pack()
                entry_sid.insert(0,"os**/os***")
                entry_sid.bind('<FocusOut>', lambda x: on_focus_out(entry_sid, "os**/os***"))
                entry_sid.bind('<FocusIn>', lambda x: on_focus_in(entry_sid))
                self.entrys.append(entry_sid)
            elif row_names[index_row].upper() == "KEEPERID":
                entry_kid = Entry(frame)
                entry_kid.pack()
                entry_kid.insert(0,"s**")
                entry_kid.bind('<FocusOut>', lambda x: on_focus_out(entry_kid, "s**"))
                entry_kid.bind('<FocusIn>', lambda x: on_focus_in(entry_kid))
                self.entrys.append(entry_kid)
            elif row_names[index_row].upper() == "OEMPID" or row_names[index_row].upper() == "ZEMPID":
                entry_oid = Entry(frame)
                entry_oid.pack()
                entry_oid.insert(0,"Enter Employee ID")
                entry_oid.bind('<FocusOut>', lambda x: on_focus_out(entry_oid, "Enter Employee ID"))
                entry_oid.bind('<FocusIn>', lambda x: on_focus_in(entry_oid))
                self.entrys.append(entry_oid)
            else:
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
        
        # if not all(entry.get() for entry in self.entrys):
        #     messagebox.showerror("Entry error", "Please fill in all information.")
        # else:
        #     pass
        if None in data:
            self.alert.config(text="Please fill in all entries!")
            return
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

    # def get_data_list(self):
    #     return self.data_update

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
    