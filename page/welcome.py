import tkinter
import time

from . import demo as PageDemo
from data import logo as DataLogo
from widget import pixel as WidgetPixel


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = 12
        board = tkinter.Canvas(self)
        board.place(x=self.winfo_width() / 2 - 12.5 * w, y=self.winfo_height() / 2 - 5 * w,
                    width=25 * w, height=10 * w)
        logo = tkinter.Canvas(board)
        logo.place(x=0, y=0, width=25 * w, height=6 * w)
        for unit in DataLogo.mokey:
            tkinter.Label(logo, bg='black').place(x=unit[0] * w, y=unit[1] * w, width=w, height=w)
            time.sleep(0.03)
            logo.update()
        slogan = tkinter.Canvas(board)
        slogan.place(x=0, y=6.8 * w, width=25 * w, height=3.2 * w)
        WidgetPixel.str_one_by_one(master=slogan, s="GITEE.COM / MONKEYHBD", x=0, y=0, w=0.25 * w,
                                   color='Black', idle=0.03)


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
