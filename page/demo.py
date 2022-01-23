import threading
import tkinter


class Page(tkinter.Canvas):
    INIT = 0
    LOADED = 1
    DESTROYED = -1

    def __init__(self, master: tkinter.Tk, bg='SystemButtonFace'):
        tkinter.Canvas.__init__(self, master, bg=bg)
        self.master = master
        self.condition = self.INIT
        self.threads: list[threading.Thread] = []

        try:  # Master is a Game Class
            self.W = master.W
        except AttributeError:
            self.W = 20

    def build(self):
        """ Page's content write in here.

        Content's master is self.

        This method should be override. """

        pass

    def deploy(self):
        """ Page's thread write in here.

        Threads should be append to self.threads. """

        pass

    def start(self):
        """ Start threads in self.threads. """

        for td in self.threads:
            td.start()

    def display(self):
        self.master.update()
        self.place(x=0, y=0, width=self.master.winfo_width(), height=self.master.winfo_height())
        self.update()
        self.build()  # Content may call self.winfo_width, so place self first.
        self.condition = self.LOADED
        self.deploy()
        self.start()
