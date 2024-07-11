from models.file import File
from models.folder import Folder

class Format:
    def __init__(self):
        self.any: str = '*'
        self.size: int = 5

class Settings:
    def __init__(self):
        self.format: Format = Format()

        self.root: Folder = Folder(".cronpy.d", True)
        self.crons: File = File(f"{self.root.path}/crons.conf", True)
