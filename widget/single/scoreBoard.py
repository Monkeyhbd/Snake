import tkinter

from widget import common as WidgetCommon


class ScoreBoard(tkinter.Canvas):
    def __init__(self, master, data):
        tkinter.Canvas.__init__(self, master, bg='Pink')
        self.data = data
        self.w = master.W
        self.box = []

    def display(self):
        w = self.w

        # <Score Board> -----------------------------------------------------------------------------------------------
        self.place(relx=0.5, x=-3 * w, rely=0.5, y=-6 * w, width=6 * w, height=12 * w)
        self.update()
        # -------------------------------------------------------------------------------------------------------------

        # <Labels> ----------------------------------------------------------------------------------------------------
        for n in range(8):
            lb = WidgetCommon.Label(self, bg='White', w=0.16 * w)
            if n < len(self.data):
                lb.text = str(self.data[n])
            lb.place(x=0.5 * w, y=w + 1.3 * n * w, width=5 * w, height=1.2 * w)
        # -------------------------------------------------------------------------------------------------------------

        # <Back Button> -----------------------------------------------------------------------------------------------
        def back_md():
            self.destroy()
        back_button = WidgetCommon.Button(master=self, text='BACK', w=0.05 * w, command=back_md)
        back_button.place(x=0, y=0, width=1.2 * w, height=0.6 * w)
