import threading
import time


class SnakeMonitor(threading.Thread):
    def __init__(self, page, snake):
        threading.Thread.__init__(self)
        self.page = page
        self.target = snake
        self.setDaemon(True)

    def run(self):
        while self.target.condition != 3:
            time.sleep(1)
        print('Dead')
        # GUIWidget.exit_init(master.current_page.root, monkeyhbd, 'single')
