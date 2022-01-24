import tkinter
import ctypes

from page import welcome as PageWelcome


class Game(tkinter.Tk):
    def __init__(self):
        try:
            # 告诉 Windows 使用程序自身的dpi适配
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except AttributeError:
            pass

        tkinter.Tk.__init__(self)
        self.tittle = 'Greedy Snake'
        self.W = 30
        self.adapt_resolution()
        self.geometry('{:d}x{:d}+20+20'.format(42 * self.W, 22 * self.W))
        self.resizable(False, False)

        self.first_page = PageWelcome

    def adapt_resolution(self):
        height = self.winfo_screenheight()

        if height >= 2160:
            self.W = 90
        elif height >= 1440:
            self.W = 50
        elif height >= 1080:
            self.W = 40
        else:
            self.W = 30

    def begin(self):
        self.first_page.init(self)
        self.first_page.display()

        self.mainloop()
