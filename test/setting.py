import tkinter

from application import demo as ApplicationDemo

from page import setting as PageSetting


if __name__ == '__main__':
    lmy = ApplicationDemo.Game()
    lmy.title('Setting Page')
    PageSetting.init(lmy)
    PageSetting.display()
    lmy.mainloop()
