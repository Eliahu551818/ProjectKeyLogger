from .writer_interface import IWriter
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class NetworkWriter(IWriter):
    
    def write(self, data: dict):
        requests.post(f"{os.environ.get('API_URL')}/data/insert_data", json=data)
        return True

