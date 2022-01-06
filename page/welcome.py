import tkinter
import time

from . import demo as PageDemo
from data import logo as DataLogo


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = 16
        board = tkinter.Canvas(self)
        board.place(x=self.winfo_width() / 2 - 12.5 * w, y=self.winfo_height() / 2 - 3 * w, width=25 * w, height=6 * w)
        for unit in DataLogo.mokey:
            tkinter.Label(board, bg='black').place(x=unit[0] * w, y=unit[1] * w, width=w, height=w)
            time.sleep(0.03)
            board.update()


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
