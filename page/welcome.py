import tkinter
import time
import random

from . import demo as PageDemo
from data import logo as DataLogo
from data import theme as DataTheme
from widget import pixel as WidgetPixel


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = 12
        board = tkinter.Canvas(self)
        board.place(relx=0.5, rely=0.5, width=25 * w, height=10 * w, anchor='center')

        logo = tkinter.Canvas(board)
        logo.place(x=0, y=0, width=25 * w, height=6 * w)
        WidgetPixel.logo_flash(master=logo, x=0, y=0, w=w, logo_info=DataLogo.mokey, colors=DataTheme.mokey_logo_colors,
                               idle=0.03, option='default')

        slogan = tkinter.Canvas(board)
        slogan.place(x=0, y=6.8 * w, width=25 * w, height=3.2 * w)
        WidgetPixel.str_one_by_one(master=slogan, s="GITEE.COM / MONKEYHBD", x=0, y=0, w=0.25 * w,
                                   color='Black', idle=0.01)


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
