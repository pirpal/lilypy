#!usr/bin/env python3

from tkinter import Frame, Text
from colors import *

class NotebookTab(Frame):
    def __init__(self, parent):
        Frame.__init__(parent)
        self.parent = parent
        self.txt = Text(
            self,
            bg=COLORS["background"],
            height=60,
            width=100
        )
        self.txt.pack()
        self.pack()
