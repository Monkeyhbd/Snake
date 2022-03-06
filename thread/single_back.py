import threading
import time

from widget.single import gameOverMessage as WidgetGameOverMessage
from widget.single import scoreBoard as WidgetScoreBoard


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

        length = self.target.len

        try:
            f = open(file='data/scoreBoard.iopt', mode='r+')
            history = eval(f.readlines()[0])
        except (IndexError, FileNotFoundError):
            f = open(file='data/scoreBoard.iopt', mode='w+')
            history = []
        history.append(length)
        history.sort(reverse=True)
        if len(history) > 10:
            history = history[: 10]
        f.seek(0)
        f.truncate()
        f.write(str(history))
        f.close()

        print(history)

        message = WidgetGameOverMessage.Message(self.page, self.target)
        message.display()

        score_board = WidgetScoreBoard.ScoreBoard(self.page, data=history)
        score_board.display()
