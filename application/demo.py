import tkinter
import time
import ctypes
import platform
import _tkinter

from page import welcome as PageWelcome


class Game(tkinter.Tk):
    def __init__(self):
        try:  # Windows
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except AttributeError:  # Linux
            pass
        except OSError:  # Happens on school's computer. (Windows 7 Python 3.6.6)
            pass

        tkinter.Tk.__init__(self)
        self.title('Greedy Snake')
        self.W = 30
        self.adapt_resolution()
        self.geometry('{:d}x{:d}+20+20'.format(42 * self.W, 22 * self.W))
        self.resizable(False, False)
        try:
            self.iconbitmap('./data/logo256.ico')
        except _tkinter.TclError:
            pass

        self['bg'] = '#E4FFDD'

        self.os = platform.system()  # What Operating System the game running on.

        self.python_version = platform.python_version()

        self.clock_resolution = time.get_clock_info('monotonic').resolution

        self.clock_accurate = True  # Linux, Mac OS, Windows 7
        if self.clock_resolution > 0.005:
            self.clock_accurate = False  # Windows 10, Windows 11

        self.first_page = PageWelcome

    def adapt_resolution(self):
        height = self.winfo_screenheight()

        if height >= 2160:
            self.W = 90
        elif height >= 1440:
            self.W = 55
        elif height >= 1080:
            self.W = 40
        else:
            self.W = 30

    def begin(self):
        self.first_page.init(self)
        self.first_page.display()

        self.mainloop()
