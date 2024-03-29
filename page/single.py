import tkinter

from . import demo as PageDemo
from data import theme as DataTheme
from widget import board as WidgetBoard
from widget import bar as WidgetBar
from widget import panel as WidgetPanel
from avatar import demo as AvatarDemo
from thread import single_back as ThreadSingleBack


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)
        self.board = None
        self.return_obj = None

    def build(self):
        w = self.W
        border_color = DataTheme.single_theme
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
        self.return_obj = WidgetBar.info_init(self)

    def deploy(self):
        w = self.W
        monkeyhbd = AvatarDemo.Snake(master=self.board, x=1, y=10, w=w, length=5, step=int(w / 5),
                                     head_color=DataTheme.snake_head, body_color=DataTheme.snake_body,
                                     len_label2=self.return_obj['len_label2'], fps_label2=self.return_obj['fps_label2'])

        WidgetPanel.panel_init(self.master, monkeyhbd)

        monitor = ThreadSingleBack.SnakeMonitor(self, monkeyhbd)

        self.threads = [monkeyhbd, monitor]


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
