#!usr/bin/env python3

import tkinter as tk
import tkinter.font as tkf
import tkinter.ttk as ttk

from colors import *
from gui_settings import *
from global_settings import *
from notebook_tab import NotebookTab

class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, X, Y))
        self.title("Lilypy v{}".format(VERSION))
        self.tabs = {}
        self.initUI()

    def initUI(self):
        self.font = tkf.Font(family="Monaco", size=11)
        self.ntb = ttk.Notebook(self)
        new_tab = tk.Frame(self.ntb)
        new_tab.pack()
        new_txt = tk.Text(
            new_tab,
            bg=COLORS["background"],
            fg=COLORS["text"],
            height=60,
            width=100,
            font=self.font
        )
        new_txt.grid()
        self.ntb.add(new_tab, text="new buffer", compound=tk.TOP)
        self.ntb.grid(row=0, column=0)
        new_tab.focus()

    
    
