import tkinter

from data import theme as DataTheme
from widget import common as WidgetCommon

from page import level as PageLevel


class Message(tkinter.Canvas):
    def __init__(self, master, snake):
        tkinter.Canvas.__init__(self, master, bg=DataTheme.exit_mess)
        self.master = master
        self.snake = snake
        self.w = master.W

    def display(self):
        w = self.w

        # <Message Box> -----------------------------------------------------------------------------------------------
        self.place(relx=0.5, x=-5 * w, rely=0.5, y=-3.75 * w, width=10 * w, height=7.5 * w)
        self.update()
        # -------------------------------------------------------------------------------------------------------------

        # <Fail Label> ------------------------------------------------------------------------------------------------
        fail_label = WidgetCommon.Label(self, text='F A I L', fg=DataTheme.exit_fail, w=0.2 * w)
        fail_label.place(x=0.3 * w, y=0.3 * w, width=9.4 * w, height=2.5 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Score Label 1> ---------------------------------------------------------------------------------------------
        score_label1 = WidgetCommon.Label(self, text='SCORE', fg=DataTheme.default, w=0.13 * w)
        score_label1.place(x=0.3 * w, y=3.1 * w, width=4.8 * w, height=2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Score Label 2> ---------------------------------------------------------------------------------------------
        score_label2 = WidgetCommon.Label(self, text=str(self.snake.level) + ' - ' + str(self.snake.len),
                                          fg=DataTheme.default, w=0.15 * w)
        score_label2.place(x=5.4 * w, y=3.1 * w, width=4.3 * w, height=2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Restart Button> --------------------------------------------------------------------------------------------
        def restart():
            page_master = self.master.master
            self.master.destroy()
            PageLevel.init(page_master)
            PageLevel.display()

        restart_button = WidgetCommon.Button(self, fg=DataTheme.default, text='RESTART', w=0.12 * w, command=restart)
        restart_button.place(x=0.3 * w, y=5.4 * w, width=5.7 * w, height=1.8 * w)

        # -------------------------------------------------------------------------------------------------------------

        # <Back Button> -----------------------------------------------------------------------------------------------
        def back():
            self.master.destroy()

        back_button = WidgetCommon.Button(self, fg=DataTheme.default, text='BACK', w=0.12 * w, command=back)
        back_button.place(x=6.3 * w, y=5.4 * w, width=3.4 * w, height=1.8 * w)
        # -------------------------------------------------------------------------------------------------------------
