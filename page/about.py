import time

from . import demo as PageDemo
from widget import common as WidgetCommon
from widget import pixel as WidgetPixel
from data import logo as DataLogo
from data import theme as DataTheme


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = self.W

        # <Snake Logo> ------------------------------------------------------------------------------------------------
        snake_logo_w = int(0.5 * w)
        snake_logo = WidgetCommon.Box(self)
        snake_logo.place(relx=0.5, x=-2.5 * snake_logo_w, y=2 * w, width=5 * snake_logo_w, height=5 * snake_logo_w)
        WidgetPixel.graphic_display(master=snake_logo, data=DataLogo.snake, w=snake_logo_w, x=0, y=0)
        # -------------------------------------------------------------------------------------------------------------

        self.update()
        time.sleep(1)
        x0 = int(-2.5 * snake_logo_w)
        idle = int(0.1 * w)
        t = 100
        for x in range(x0, x0 - t * idle, -idle):
            snake_logo.place(x=x)
            self.update()
            time.sleep(0.01)

        # <Snake Logo Text> -------------------------------------------------------------------------------------------
        snake_logo_text_w = int(0.5 * w)
        snake_logo_text = WidgetCommon.Box(self)
        snake_logo_text.place(relx=0.55, x=-16.5 * snake_logo_text_w, y=2 * w,
                              width=33 * snake_logo_text_w, height=5 * snake_logo_text_w)
        WidgetPixel.str_one_by_one(master=snake_logo_text, s='S N A K E', x=0, y=0, w=snake_logo_text_w,
                                   color=DataTheme.snake_logo, idle=0.1)
        # -------------------------------------------------------------------------------------------------------------

        # <Introduction> ----------------------------------------------------------------------------------------------
        introduction = WidgetCommon.Box(self)
        introduction.place(relx=0.5, x=-12.5 * w, y=7 * w, width=25 * w, height=1.5 * w)
        WidgetPixel.str_one_by_one(master=introduction, s='A CLASSICAL GREEDY SNAKE GAME.', x=0.25 * w, y=0, w=0.18 * w,
                                   color='Black', idle=0.05)
        # -------------------------------------------------------------------------------------------------------------


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
