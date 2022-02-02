import tkinter

from . import demo as PageDemo
from widget import board as WidgetBoard
from widget import bar as WidgetBar
from data import theme as DataTheme
from thread import level_back as ThreadLevelBack


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)
        self.board = None
        self.fps_label2 = None
        self.len_label2 = None

    def build(self):
        w = self.W
        border_color = DataTheme.level_theme
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=0,
                                                   width=self.winfo_width(),
                                                   height=w)
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=self.winfo_height() - w,
                                                   width=self.winfo_width(),
                                                   height=w)
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=w,
                                                   width=w,
                                                   height=self.winfo_height() - 2 * w)
        tkinter.Label(self, bg=border_color).place(x=self.winfo_width() - w,
                                                   y=w,
                                                   width=w,
                                                   height=self.winfo_height() - 2 * w)

        self.board = WidgetBoard.Board(self, 20, 40)
        self.board.display()
        rtn = WidgetBar.info_init(self)
        self.len_label2 = rtn['len_label2']
        self.fps_label2 = rtn['fps_label2']

    def deploy(self):
        self.threads.append(ThreadLevelBack.Back(self))


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
