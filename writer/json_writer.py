from .writer_interface import IWriter
import json
import os

class JsonWriter(IWriter):
    
    def write(self, data: dict) -> bool:
        '''
        Parameter:
        data (dict):
            {
                "time":"datetime format",
                "data": {
                    "WindowUsed": string of data,
                    "Chrome":"ghbibubjbkd ddsx"
                },
                "mac_address":"4564.445"
            }
        '''

        assert ("time" in data) and ("data" in data)
        
        time: str = data.get("time")
        target_id : str = data.get("mac_address")
        new_data: dict = data.get("data")
        path: str = os.path.abspath(f"./data/{target_id}.json")

        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump({}, f)

        # Read existing data
        with open(path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}  # Handle empty or corrupted files

        # Update the data structure
        for window, value in new_data.items():
            if window not in data:
                data[window] = {}
            data[window][time] = value

        # Write back to the file
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

        return True


    

