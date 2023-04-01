from tkinter import *
from functools import partial
from ..database import *
from . import *
from .AddWindow import AddWindow
from .ShowWindow import ShowWindow
import time



class Category(Frame):
    def __init__(self, master):
        super().__init__(master)
        #a list to delete data later
        self.del_data = []

    def config(self, data, table):
        self.colnames, result = data
        self.mainframe = Frame(self)
        self.mainframe.pack(fill=BOTH)

        self.table = Table(self.mainframe, self.colnames, table)
        self.table.add_list_data(self.colnames, result)
        self.table.pack(fill = X)
        self.bottom = Frame(self.mainframe)
        self.bottom.pack(side = LEFT)
        

        Button(self.bottom, text="Add",command=partial(self.add_handle,self.colnames)).pack(side=LEFT)
        Button(self.bottom, text="Show", command=partial(self.show_handle)).pack(side=LEFT)
        Button(self.bottom, text="Edit", command=partial(self.repair_handle)).pack(side=LEFT)
        Button(self.bottom, text="Delete", command=partial(self.delete_handle)).pack(side=LEFT)
        Button(self.bottom, text="Apply", command=partial(self.apply_handle)).pack(side=LEFT)
        self.infoframe = Frame(self.bottom, width=20)
        self.infoframe.pack(side=RIGHT)

        self.alert = Label(self.infoframe, text="")
        self.alert.pack(side=LEFT)

    def add_handle(self,colnames):
        self.add_win = AddWindow("Add")
        self.add_win.add_widget(colnames)
        self.add_win.set_table(self.table)
        self.add_win.set_alert(self.alert)

    def show_handle(self):
        details = self.table.select_values
        show_win = ShowWindow(details[1])
        show_win.config(self.colnames,details)
        
    def repair_handle(self):
        details = self.table.select_values
        self.repair_win = AddWindow("Repair")
        self.repair_win.add_widget(self.colnames)
        self.repair_win.set_table(self.table)
        self.repair_win.change2repair()
        self.repair_win.insert_data(details)
        #set alert to repair_win

    def delete_handle(self):
        self.del_data = []
        item = self.table.select_item
        cols = self.table.cols
        values = self.table.select_values
        self.del_data.append([self.table.name, cols[0] ,values[0]])
        self.table.treev.delete(item)
        self.alert.config(text= f"Delete {values[0]} success!!!")

    def apply_handle(self):
        #add
        try: 
            list_data = self.add_win.data_update
            table = self.add_win.table.name
            for data in list_data:
                    temp_tuple = tuple(data.values())
                    for i in range(len(temp_tuple)):
                        try:
                            temp_tuple[i] = int(temp_tuple[i])
                        except:
                            pass
                        else:
                            temp_tuple[i] = str(temp_tuple[i])
                    insert_one(table, temp_tuple)
        except:
            pass

        #edit
        list_data = self.repair_win.data_update
        table = self.repair_win.table.name    
        for data in list_data:
                temp_tuple = tuple(data.values())
                for i in range(len(temp_tuple)):
                    try:
                        temp_tuple[i] = int(temp_tuple[i])
                    except:
                        pass
                    else:
                        temp_tuple[i] = str(temp_tuple[i])
                update_one(table,self.colnames ,temp_tuple)


        #del

        try:
            list_data = self.del_data
            for data in list_data:
                del_one(data[0], data[1], data[2])
        except:
            pass
        self.alert.config(text = "Apply done!!!")


class Home(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.main_bg = PhotoImage(file="image/Home_screen.png").subsample(1)
        self.main_frame = Label(self, image = self.main_bg)
        self.main_frame.pack(fill=BOTH, expand=True)



class AnimalCategory(Category):
    def __init__(self, master):
        super().__init__(master)

    def config(self, data, table):
        super().config(data, table)
        Button(self.bottom, text="Feeding", command=partial(self.feeding)).pack(side = LEFT)

    def feeding(self):
        top = Toplevel()
        top.title("Feeding")
        colnames, result = show_all_feeding()
        top_table = Table(top, colnames, None)
        top_table.add_list_data(colnames, result)
        top_table.pack(side="top")
        frame = Frame(top)
        frame.pack(side="bottom")
        button = Button(frame, text="Add", command=partial(self.add_feeding,colnames)).pack()  

    def add_feeding(self,cols):
        self.add_feeding_win = AddWindow("Add")
        self.add_feeding_win.add_widget(cols)
        # self.add_feeding_win.set_table(self.table)

class EmployeeCategory(Category):
    def __init__(self, master):
        super().__init__(master)

    def config(self, data, table):
        super().config(data, table)

        Button(self.bottom, text="Ostaff", command=partial(self.Ostaff)).pack(side = LEFT)
        Button(self.bottom, text="Zookeeper", command=partial(self.Zookeeper)).pack(side = LEFT)    

    def add_zookeeper(self):
        colnames = get_col_zookeeper()
        self.add_zookeeper_win = AddWindow("Add Zookeeper")
        self.add_zookeeper_win.add_widget(colnames)
        self.add_zookeeper_win.set_table(Table(None,colnames,'ZOOKEEPER'))
        self.add_zookeeper_win.set_alert(self.alert)

    def add_ostaff(self):
        colnames = get_col_ostaff()
        self.add_ostaff_win = AddWindow("Add Ostaff")
        self.add_ostaff_win.add_widget(colnames)
        self.add_ostaff_win.set_table(Table(None,colnames,'OSTAFF'))
        self.add_ostaff_win.set_alert(self.alert)

    def Ostaff(self):
        top = Toplevel()
        top.title("Ostaff Info")
        colnames, result = show_all_info_ostaff()
        top_table = Table(top, colnames, None)
        top_table.add_list_data(colnames, result)
        top_table.pack(side="top")
        frame = Frame(top)
        frame.pack(side="bottom")
        button = Button(frame, text="Add_Ostaff", command=partial(self.add_ostaff)).pack()    
        button = Button(frame, text="Apply", command=partial(self.apply_handle)).pack()   
    def Zookeeper(self):
        top = Toplevel()
        top.title("Zookeeper Info")
        colnames, result = show_all_info_zookeeper()
        top_table = Table(top, colnames, None)
        top_table.add_list_data(colnames, result)
        top_table.pack(side="top")
        frame = Frame(top)
        frame.pack(side="bottom")
        button = Button(frame, text="Zskills", command=partial(self.Zskills)).pack()
        button = Button(frame, text="Add_Zookeeper", command=partial(self.add_zookeeper)).pack()
        button = Button(frame, text="Apply", command=partial(self.apply_handle)).pack()  

    def Zskills(self):
        top = Toplevel()
        top.title("Zookeeper Zskills")
        colnames, result = show_all_zskills()
        top_table = Table(top, colnames, None)
        top_table.add_list_data(colnames, result)
        top_table.pack(side="top")

class VisitorCategory(Category):
    def __init__(self, master):
        super().__init__(master)

    def config(self, data, table):
        super().config(data, table)
        Button(self.bottom, text="Information", command=partial(self.Infomation)).pack(side = LEFT)
    
    def Infomation(self):
        top = Toplevel()
        top.title("Infomation")
        colnames, result = show_all_info_visitor()
        top_table = Table(top, colnames, None)
        top_table.add_list_data(colnames, result)
        top_table.pack(side="top")
