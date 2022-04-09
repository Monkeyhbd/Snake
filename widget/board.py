import tkinter

from . import  common as WidgetCommon


class Board(tkinter.Canvas):
    def __init__(self, master, h, w):
        tkinter.Canvas.__init__(self, master)
        self.master = master
        self.w = w
        self.h = h
        self.W = master.W
        self.size = [w, h]
        self['bg'] = '#BBFFAA'

        self.border: list = []
        self.wall: list = []

        self.background = WidgetCommon.Box(self)

        for a in range(h):
            self.border.append([-self.master.W, a * self.master.W])  # W
            self.border.append([w * self.master.W, a * self.master.W])  # E
        for b in range(w):
            self.border.append([b * self.master.W, -self.master.W])  # N
            self.border.append([b * self.master.W, h * self.master.W])  # S

    def build(self):
        width = self.master.W
        self.background.place(x=0, y=0, relwidth=1, relheight=1)
        for a in range(self.h):
            for b in range(self.w):
                if a % 2 - b % 2 == 0:
                    tkinter.Label(self.background, bg='#E4FFDD').place(x=b * width, y=a * width,
                                                                       width=width, height=width)
                    self.update()

    def display(self):
        self.place(x=self.master.W, y=self.master.W, width=self.w * self.master.W, height=self.h * self.master.W)
        self.build()
