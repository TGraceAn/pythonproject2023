from tkinter import *
from tkinter import ttk
from functools import partial
import os

class ShowWindow(Toplevel):
    def __init__(self, title):
        super().__init__()

    def config(self, columns : list, details : list):
        detail_frame = Frame(self)
        detail_frame.pack(side=RIGHT)
        right_frame = Frame(self, width = 40)
        right_frame.pack(side=RIGHT)
        top_frame = Frame(self, height = 20)
        top_frame.pack(side=TOP)
        img_frame = Frame(self)
        img_frame.pack(side=RIGHT, expand= True)
        bottom_frame = Frame(self, height = 20)
        bottom_frame.pack(side=BOTTOM)
        left_frame = Frame(self, width = 20)
        left_frame.pack(side=LEFT)
        try:
            self.img = PhotoImage(file=f"image/{details[0]}.png").subsample(2)
        except:
            self.img = PhotoImage(file="image/default.png").subsample(2)
        Label(img_frame,image=self.img).pack()
        for index in range(0,len(columns)):
            text = str(columns[index]) + " : " + str(details[index])
            label = Label(detail_frame, text=text)
            label.pack()
