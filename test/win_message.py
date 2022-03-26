from application import demo as ApplicationDemo
from widget.level import winMessage as WinMessage

if __name__ == '__main__':
    lmy = ApplicationDemo.Game()
    message = WinMessage.Message(lmy)
    message.display()
    lmy.mainloop()
