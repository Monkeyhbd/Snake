import tkinter

from page import main3 as PageMain


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('1260x660')
    lmy.title('Main Page')
    PageMain.init(lmy)
    PageMain.page_instance.W = 30
    PageMain.display()
    lmy.mainloop()
