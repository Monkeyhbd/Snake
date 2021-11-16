import module.graphic.environment as GUIEnvironment
import module.graphic.basic as GUIBasic
import module.graphic.page as GUIPage

W = GUIBasic.W


if __name__ == '__main__':
    lmy = GUIEnvironment.window
    GUIPage.welcome_page(lmy)
    lmy.mainloop()
