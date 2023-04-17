from tkinter import *
from functools import partial
import threading

class Navigation(Frame):
    def __init__(self, master, navs, details):
        super().__init__(master)
        self.img = PhotoImage(file='image/tri.png').subsample(30)
        self.config(navs, details)

    def config(self,buttons, details):
        width = max([len(i) for i in buttons])
        self.buttons = []
        for index in range(len(buttons)):
            self.detail_frame = Frame(details, height = 20, bg="#4a536b")
            self.detail_frame.pack(fill = X)
            self.dash_frame = Frame (details, bg = '#4a536b')
            self.dash_frame.pack(fill = X)
            self.frame0 = Frame(self.dash_frame, bg = '#4a536b', width = 20)
            self.frame0.pack(side = LEFT, fill = X)
            self.frame1 = Frame(self.dash_frame, bg = '#4a536b')
            self.frame1.pack(side = LEFT, fill = X)
            self.frame2 = Frame(self.dash_frame, bg = '#4a536b', width = 20)
            self.frame2.pack(side = RIGHT, fill = X)
            button = buttons[index]
            but = Button(self.frame1, text=button.upper(), padx=4 ,pady=4, width=width, bg = '#4a536b', foreground= 'black', activebackground= '#4a536b', activeforeground= '#4a536b', relief=FLAT, borderwidth=0)
            label = Label(self.frame2,image=self.img,bg = '#FFFFFF', background= '#4a536b', foreground= "#000000")
            but.pack(side=RIGHT)
            but.config(command=partial(self.button_handle, index))
            self.buttons.append([but, label])

    def button_handle(self, index : Label):
        label = self.buttons[index][1]
        if label.winfo_viewable():
            label.pack_forget()
        else:
            self.check(index)
            label.pack(side=RIGHT)

        dash = self.buttons[index][2]
        if dash.winfo_viewable():
            dash.pack_forget()
        else:
            self.check(index)
            dash.pack(fill = BOTH, expand = True)

    def map_dash(self):
        for index in range(0, len(self.buttons)):
            self.buttons[index].append(self.dash_list[index])

        self.buttons[0][1].pack(side=BOTTOM)
        self.buttons[0][2].pack(side=BOTTOM)

    def set_dash(self, dash_list):
        self.dash_list = dash_list
        self.map_dash()



    def check(self, index):
        for _index in range(0, len(self.buttons)):
            if _index != index:
                if self.buttons[_index][1].winfo_viewable():
                    self.buttons[_index][1].pack_forget()
                if self.buttons[_index][2].winfo_viewable():
                    self.buttons[_index][2].pack_forget()



if __name__ == "__main__":
    win = Tk()
    img = PhotoImage(file='tri.png')
    Navigation(win).pack(fill=BOTH)
    win.mainloop()