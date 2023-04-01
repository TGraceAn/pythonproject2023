from tkinter import *
from src import *

#create a list for navigation
navs = ["Home","Person Details", "Animals Details", "Employee Details", "Visitor Details", "Exhibit"]

class Management:
    def __init__(self, root, navs):
        self.window = root
        self.window.title("Zoo Management System")
        self.detail_frame = Frame(self.window, bg="#4a536b")
        self.detail_frame.pack(side=LEFT, fill= Y)

        self.Zoo_logo = PhotoImage(file="image/Zoo_Logo.png").subsample(18)
        self.Zoo_logo_label = Label(self.detail_frame, image=self.Zoo_logo, bg= "#4a536b")
        self.Zoo_logo_label.pack(fill=X)

        self.user_frame = Frame(self.window, bg="#228B22", height= 30)
        self.user_frame.pack(side=TOP, fill=X)

        self.text = PhotoImage(file="image/default_text.png").subsample(2)
        self.label = Label(self.window, image=self.text)
        self.label.pack(anchor="center")

        self.main_bg = PhotoImage(file="image/main.png").subsample(2)
        self.main_frame = Label(self.window, image = self.main_bg)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.nav = Navigation(self.window, navs, self.detail_frame)
        self.nav.pack()


        self.dash_list = []
        home_dash = Home(self.main_frame)
        self.dash_list.append(home_dash)
        
        person_dash = Category(self.main_frame)
        person_dash.config(get_all('PERSON'),'PERSON')
        self.dash_list.append(person_dash)
        
        #get all data from database
        animal_dash = AnimalCategory(self.main_frame)
        animal_dash.config(get_all('ANIMAL'),'ANIMAL')
        self.dash_list.append(animal_dash)

        employee_dash = EmployeeCategory(self.main_frame)
        employee_dash.config(get_all('EMPLOYEE'),'EMPLOYEE')
        self.dash_list.append(employee_dash)

        visitor_dash = VisitorCategory(self.main_frame)
        visitor_dash.config(get_all('VISITOR'),'VISITOR')
        self.dash_list.append(visitor_dash)
        
        ex_dash = Category(self.main_frame)
        ex_dash.config(get_all('EXHIBIT'), 'EXHIBIT')
        self.dash_list.append(ex_dash)

        # set default dashboard
        self.nav.set_dash(self.dash_list)


        
        
            

if __name__ == "__main__":
    window = Tk()
    app = Management(window, navs)
    window.mainloop()