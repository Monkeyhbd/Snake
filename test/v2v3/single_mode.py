import tkinter

from page import single as PageSingle


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    lmy.title('Main Page')
    PageSingle.init(master=lmy)
    PageSingle.display()
    lmy.mainloop()
