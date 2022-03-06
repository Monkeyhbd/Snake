import tkinter

from . import pixel as WidgetPixel


class Button(tkinter.Canvas):
    """ Button widget to display a mokey style's button with pixel font text. """

    place_backup = tkinter.Canvas.place

    def __init__(self, master, bg='White', active_background='LightGrey', fg='Black', text='', w=1, command=None):
        tkinter.Canvas.__init__(self, master, bg=bg)
        self.master = master
        if bg is None:
            self['bg'] = master['bg']
        else:
            self['bg'] = bg
        self.active_background = active_background
        self.fg = fg
        self.text = text
        self.w = w
        self.command = command

        def cmd(_):
            command()

        self.cmd = cmd

        def enter(_):
            self['bg'] = active_background

        def leave(_):
            self['bg'] = bg

        self.bind('<Enter>', enter)
        self.bind('<Leave>', leave)
        if command is not None:
            self.bind('<ButtonPress-1><ButtonRelease-1>', cmd)

    def place(self, *args, **kwargs):
        self.place_backup(*args, **kwargs)
        self.update()
        rtn = WidgetPixel.str_middle(self, s=self.text, x=0, y=0, width=self.winfo_width(),
                                     height=self.winfo_height(), w=self.w, color=self.fg)
        if self.command is not None:
            for label in rtn:
                label.bind('<ButtonPress-1><ButtonRelease-1>', self.cmd)


class Label(tkinter.Canvas):
    """ Label widget to display a mokey style's label with pixel font text. """

    place_backup = tkinter.Canvas.place

    def __init__(self, master, bg='White', fg='Black', text='', w=1):
        tkinter.Canvas.__init__(self, master, bg=bg)
        self.master = master
        if bg is None:
            self['bg'] = master['bg']
        else:
            self['bg'] = bg
        self.fg = fg
        self.text = text
        self.w = w

    def place(self, *args, **kwargs):
        self.place_backup(*args, **kwargs)
        self.update()
        WidgetPixel.str_middle(self, s=self.text, x=0, y=0, width=self.winfo_width(),
                               height=self.winfo_height(), w=self.w, color=self.fg)


class Box(tkinter.Frame):
    """ Box widget to include other widget. """

    def __init__(self, master, bg=None):
        tkinter.Frame.__init__(self, master, highlightthickness=0)

        if bg is None:
            self['bg'] = master['bg']
        else:
            self['bg'] = bg
