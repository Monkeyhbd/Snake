import tkinter

from page import welcome as PageWelcome


if __name__ == '__main__':
    lmy = tkinter.Tk()
    lmy.geometry('840x440')
    lmy.title('Welcome Page')
    PageWelcome.init(master=lmy)
    PageWelcome.display()
    lmy.mainloop()
