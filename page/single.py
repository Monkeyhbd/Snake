import tkinter

from . import demo as PageDemo
from data import theme as DataTheme
from widget import board as WidgetBoard
from widget import bar as WidgetBar


W = 20


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        border_color = DataTheme.single_theme
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=0,
                                                   width=self.winfo_width(),
                                                   height=W)
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=self.winfo_height() - W,
                                                   width=self.winfo_width(),
                                                   height=W)
        tkinter.Label(self, bg=border_color).place(x=0,
                                                   y=W,
                                                   width=W,
                                                   height=self.winfo_height() - 2 * W)
        tkinter.Label(self, bg=border_color).place(x=self.winfo_width() - W,
                                                   y=W,
                                                   width=W,
                                                   height=self.winfo_height() - 2 * W)

        board = WidgetBoard.board_init(self, 20, 40)
        return_obj = WidgetBar.info_init(self)

        """monkeyhbd = GUISnake.Snake(board, 1, 10, 15,
                                   DataTheme.snake_head, DataTheme.snake_body,
                                   int(W / 5), return_obj['len_label2'], return_obj['fps_label2'], [])
        GUIWidget.panel_init(master, monkeyhbd)
        monkeyhbd.setDaemon(True)
        monkeyhbd.start()

        GUIBack.single_back_create(master, monkeyhbd)"""


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
