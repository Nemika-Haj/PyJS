class createReadStream:
    def __init__(self, path:str):
        self.path = path

    def chunk(self):
        return open(self.path, "r").read()
    
class createWriteStream:
    def __init__(self, path:str):
        self.path = path

    def write(self, _data:str):
        with open(self.path, "w+") as f:
            f.write(_data)