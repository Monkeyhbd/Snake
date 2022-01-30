import tkinter

from page import mainChristmas as PageMain


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    lmy.title('Main Page')
    PageMain.init(master=lmy)
    PageMain.display()
    lmy.mainloop()
