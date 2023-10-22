import json

class JsonManager:
    def __init__(self):
        pass

    def writeJson(self, data, path):
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    def readJson(self, path):
        with open(path, 'r') as file:
            data = json.load(file)
            return data
