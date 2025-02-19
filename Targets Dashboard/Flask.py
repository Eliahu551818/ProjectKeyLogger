from flask import Flask, jsonify
from flask_cors import CORS
import os

path = r'C:\Users\orzel\Downloads\new'

app = Flask(__name__)
CORS(app)

@app.route('/list_targets')
def list_targets():
    return jsonify(os.listdir(path))

if __name__ == '__main__':
    app.run()