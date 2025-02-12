import yaml
import os
from writer_interface import IWriter

class YamlWriter(IWriter):
    def write(self, data: dict, target_id: str = "0"):
        '''
            Parameter:
            data (dict):
                {
                    "time":"datetime format",
                    "data": {
                        "WindowUsed": string of data,
                    "Chrome":"ghbibubjbkd ddsx"
                }
            }
            '''

        assert ("time" in data) and ("data" in data)
        
        time: str = data.get("time")
        new_data: dict = data.get("data")
        path: str = os.path.abspath(f"./data/{target_id}.json")

        # Ensure file exists
        if not os.path.exists(path):
            with open(path, 'w') as f:
                yaml.dump({}, f)

        # Read the existing YAML file
        with open(path, 'r') as file:
            try:
                data = yaml.safe_load(file) or {}  # Load YAML, handle empty file
            except yaml.YAMLError:
                data = {}

        # Update the YAML structure
        for window, value in new_data.items():
            if window not in data:
                data[window] = {}
            data[window][time] = value

        # Write back to YAML file
        with open(path, 'w') as file:
            yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

        return True
