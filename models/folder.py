import os

class Folder:
    def __init__(self, path: str, create: bool):
        self.path: str = path
        self.create: bool = create
        self.exists: bool = os.path.isdir(path)

        self._load()

    def _load(self):
        if (self.exists == False and self.create == True):
            os.mkdir(self.path)
