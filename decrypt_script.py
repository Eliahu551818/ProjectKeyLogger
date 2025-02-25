import os
import json
from encryption.shaul_encryption import Encryption

e = Encryption()

with open(os.path.abspath("./data/0.json")) as f:
   data: dict = json.load(f)
   
for key, value in data.items():
    print(f"Key: {key}")
    for timestamp, list_of_keys in value.items():
        print(f"  Timestamp: {timestamp}")
        for char in list_of_keys:
            if e.decrypt(char) == 'Key.enter':
                print(e.decrypt(char))

