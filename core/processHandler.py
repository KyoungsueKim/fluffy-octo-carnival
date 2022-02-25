import threading
import pygetwindow as gw


def getWindow(dialog):
    thread = GetWindow(dialog)
    thread.daemon = True
    thread.start()


class GetWindow(threading.Thread):
    def __init__(self, dialog):
        super(GetWindow, self).__init__()
        self.dialog = dialog

    def run(self):
        windows = gw.getWindowsWithTitle('Z9★ 온라인')[0]
        print(windows)
