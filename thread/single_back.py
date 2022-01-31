import threading
import time

from widget.single import gameOverMessage as WidgetGameOverMessage


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
        # WidgetGameOverMessage.exit_init(self.page, self.target, 'single')
        message = WidgetGameOverMessage.Message(self.page, self.target)
        message.display()
