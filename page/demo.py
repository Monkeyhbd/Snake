import threading
import tkinter


class Page(tkinter.Canvas):
    INIT = 0
    PRELOADED = 1
    LOADED = 2
    DESTROYED = -1

    def __init__(self, master: tkinter.Tk, bg=None):
        tkinter.Canvas.__init__(self, master)
        if bg is not None:
            self['bg'] = bg
        else:
            self['bg'] = master['bg']
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
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.update()
        self.build()  # Content may call self.winfo_width, so place self first.
        self.condition = self.LOADED
        self.deploy()
        self.start()

    def hangup(self):
        pass

    def preload(self):
        pass

    def reload(self):
        pass
