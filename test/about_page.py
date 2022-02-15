import tkinter

from page import about as PageAbout


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('1260x660')
    lmy.title('About Page')
    PageAbout.init(lmy)
    PageAbout.page_instance.W = 30
    PageAbout.display()
    lmy.mainloop()
