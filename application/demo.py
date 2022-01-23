import tkinter

from page import welcome as PageWelcome


class Game(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.tittle = 'Greedy Snake'
        self.W = 30
        self.geometry('{:d}x{:d}+20+20'.format(42 * self.W, 22 * self.W))
        self.resizable(False, False)

        self.first_page = PageWelcome

    def begin(self):
        self.first_page.init(self)
        self.first_page.display()

        self.mainloop()
