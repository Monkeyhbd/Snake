import platform

from . import demo as PageDemo
from widget import common as WidgetCommon


class Page(PageDemo.Page):
    def __init__(self, master):
        PageDemo.Page.__init__(self, master=master)

    def build(self):
        w = self.W

        # <Back> ------------------------------------------------------------------------------------------------------
        def back_button_md():
            self.destroy()

        back_button = WidgetCommon.Button(self, text='BACK', w=0.1 * w, command=back_button_md)
        back_button.place(x=0.5 * w, y=0.5 * w, width=2.8 * w, height=1.2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Tittle> ----------------------------------------------------------------------------------------------------
        tittle = WidgetCommon.Label(self, text='SETTING', w=0.2 * w)
        tittle.place(relx=0.5, x=-5 * w, y=1 * w, width=10 * w, height=2.4 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Container> -------------------------------------------------------------------------------------------------
        container = WidgetCommon.Box(self, bg='White')
        container.place(relx=0.5, x=-15 * w, y=4 * w, width=30 * w, height=16 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <System Information> ----------------------------------------------------------------------------------------
        system_info1 = WidgetCommon.Label(container, text='OS TYPE:', w=0.1 * w, align='left', bg=None)
        system_info1.place(x=9 * w, y=3 * w, height=1.4 * w, width=5 * w)
        system_info2 = WidgetCommon.Label(container, text=platform.system().upper(), w=0.1 * w, align='left', bg=None)
        system_info2.place(x=16 * w, y=3 * w, height=1.4 * w, width=5 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Interpreter Information> -----------------------------------------------------------------------------------
        interpreter_info1 = WidgetCommon.Label(container, text='INTERPRETER:', w=0.08 * w, align='left', bg=None)
        interpreter_info1.place(x=9 * w, y=4.6 * w, height=1.4 * w, width=5 * w)
        interpreter_info2 = WidgetCommon.Label(container, text=platform.python_version().upper(),
                                               w=0.1 * w, align='left', bg=None)
        interpreter_info2.place(x=16 * w, y=4.6 * w, height=1.4 * w, width=5 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Game Information> ------------------------------------------------------------------------------------------
        game_info1 = WidgetCommon.Label(container, text='GAME VERSION:', w=0.08 * w, align='left', bg=None)
        game_info1.place(x=9 * w, y=6.2 * w, height=1.4 * w, width=5 * w)
        game_info2 = WidgetCommon.Label(container, text='3.0.0',
                                        w=0.1 * w, align='left', bg=None)
        game_info2.place(x=16 * w, y=6.2 * w, height=1.4 * w, width=5 * w)
        # -------------------------------------------------------------------------------------------------------------


page_instance: Page


def init(master):
    global page_instance
    page_instance = Page(master=master)


def display():
    global page_instance
    page_instance.display()
