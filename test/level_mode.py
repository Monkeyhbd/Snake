import tkinter

from page import level as PageLevel


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    lmy.title('Level Mode')
    PageLevel.init(master=lmy)
    PageLevel.display()
    lmy.mainloop()
