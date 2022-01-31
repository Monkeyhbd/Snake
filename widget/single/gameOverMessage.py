import tkinter

from data import theme as DataTheme
from widget import common as WidgetCommon


class Message(tkinter.Canvas):
    def __init__(self, master, snake):
        tkinter.Canvas.__init__(self, master, bg=DataTheme.exit_mess)
        self.master = master
        self.snake = snake
        self.w = master.W

    def display(self):
        w = self.w

        # <Message Box> -----------------------------------------------------------------------------------------------
        self.place(relx=0.5, x=-5 * w, rely=0.5, y=-5 * w, width=10 * w, height=10 * w)
        self.update()
        # -------------------------------------------------------------------------------------------------------------

        # <Game Over Label> -------------------------------------------------------------------------------------------
        game_over_label = WidgetCommon.Label(self, text='GAME OVER', fg=DataTheme.exit_win, w=0.2 * w)
        game_over_label.place(x=0.3 * w, y=0.3 * w, width=9.4 * w, height=2.5 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Score Label 1> ---------------------------------------------------------------------------------------------
        score_label1 = WidgetCommon.Label(self, text='SCORE', fg=DataTheme.default, w=0.15 * w)
        score_label1.place(x=0.3 * w, y=3.1 * w, width=4.8 * w, height=2.2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Score Label 2> ---------------------------------------------------------------------------------------------
        score_label2 = WidgetCommon.Label(self, text=str(self.snake.len), fg=DataTheme.default, w=0.15 * w)
        score_label2.place(x=5.4 * w, y=3.1 * w, width=4.3 * w, height=2.2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Back Button> -----------------------------------------------------------------------------------------------
        def back(_):
            self.master.destroy()

        back_button = WidgetCommon.Button(self, fg=DataTheme.default, text='B A C K', w=0.15 * w, command=back)
        back_button.place(x=0.3 * w, y=5.6 * w, width=9.4 * w, height=1.9 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Restart Button> --------------------------------------------------------------------------------------------
        restart_button = WidgetCommon.Button(self, fg=DataTheme.default, text='RESTART', w=0.15 * w)
        restart_button.place(x=0.3 * w, y=7.8 * w, width=9.4 * w, height=1.9 * w)
        # -------------------------------------------------------------------------------------------------------------
