import tkinter
import time

from data import theme as DataTheme
from data import logo as DataLogo
from widget import common as WidgetCommon
from widget import pixel as WidgetPixel


class Message(tkinter.Canvas):
    def __init__(self, master):
        tkinter.Canvas.__init__(self, master, bg=DataTheme.exit_mess)
        self.master = master
        self.w = master.W

    def display(self):
        w = self.w

        # <Message Box> -----------------------------------------------------------------------------------------------
        self.place(relx=0.5, x=-5 * w, rely=0.5, y=-3.75 * w, width=10 * w, height=7.5 * w)
        self.update()
        # -------------------------------------------------------------------------------------------------------------

        # <Stage> ------------------------------------------------------------------------------------------------
        stage = WidgetCommon.Label(self, fg=DataTheme.exit_fail, w=0.2 * w)
        stage.place(x=0.3 * w, y=1.4 * w, width=9.4 * w, height=4.8 * w)
        # -------------------------------------------------------------------------------------------------------------

        # {Logo} ------------------------------------------------------------------------------------------------------
        logo_container = WidgetCommon.Box(master=stage)
        logo_container.place(x=2.2 * w, y=1.65 * w, width=5 * w, height=1.2 * w)
        WidgetPixel.logo_flash(master=logo_container, x=0, y=0, w=0.2 * w,
                               logo_info=DataLogo.mokey, colors=DataTheme.mokey_logo_colors,
                               idle=0.04)
        for y in range(26):
            logo_container.place(y=1.65 * w - 0.04 * w * y)
            time.sleep(0.02)
            stage.update()
        time.sleep(0.3)
        # -------------------------------------------------------------------------------------------------------------

        # <Success> ---------------------------------------------------------------------------------------------------
        success = WidgetPixel.str_one_by_one(stage, s='SUCCESS', x=1.3 * w, y=2.8 * w, w=0.2 * w,
                                             color='Red', idle=0.02)
        # -------------------------------------------------------------------------------------------------------------

        # {Stage} -----------------------------------------------------------------------------------------------------
        for y in range(21):
            stage.place(y=1.4 * w - y * 0.055 * w)
            time.sleep(0.02)
            stage.update()
        # -------------------------------------------------------------------------------------------------------------

        # <Back Button> -----------------------------------------------------------------------------------------------
        def back():
            self.master.destroy()

        back_button = WidgetCommon.Button(self, fg=DataTheme.default, text='BACK', w=0.12 * w, command=back)
        back_button.place(x=0.3 * w, y=5.4 * w, width=9.4 * w, height=1.8 * w)
        # -------------------------------------------------------------------------------------------------------------
