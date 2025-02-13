from writer_interface import IWriter
import requests
import json
import os


class NetworkWriter(IWriter):
    
    def write(self, data: dict, target_id: str = "0"):
        json_data = json.dumps(data)
        response = requests.post(os.environ.get("DATA_SERVER_URL"), data={"data": json_data, "target_id": target_id})

        return response.text