import tkinter


class Page(tkinter.Canvas):
    INIT = 0
    LOADED = 1
    DESTROYED = -1

    def __init__(self, master: tkinter.Tk, bg='SystemButtonFace'):
        tkinter.Canvas.__init__(self, master, bg=bg)
        self.master = master
        self.condition = self.INIT

    def build(self):
        """ Page's content write in here.

        Content's master is self.

        This method should be override. """

        pass

    def display(self):
        self.master.update()
        self.place(x=0, y=0, width=self.master.winfo_width(), height=self.master.winfo_height())
        self.update()
        self.build()  # Content may call self.winfo_width, so self place first.
        self.condition = self.LOADED
