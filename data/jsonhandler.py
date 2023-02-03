import json


class JsonHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def write_json(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def read_json(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)