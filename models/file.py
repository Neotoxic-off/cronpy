import os

class File:
    def __init__(self, path: str, create: bool):
        self.path: str = path
        self.create: bool = create
        self.exists: bool = os.path.isfile(path)
        self.content: list = []

        self._load()

    def _load(self):
        if (self.exists == False):
            if (self.create == True):
                open(self.path, 'a').close()
        else:
            self._read()

    def _read(self):
        if (self.exists == True):
            with open(self.path, "r") as f:
                self.content = f.readlines()
