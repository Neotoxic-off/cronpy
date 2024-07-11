import json

from src.settings import Settings
from src.interpreter import Interpreter

class Core:
    def __init__(self):
        self.settings: Settings = Settings()
        self.interpreter: Interpreter = Interpreter(self.settings)
        
        self._run()

    def _run(self):
        results: list = []
        result: dict = {}

        for line in self.settings.crons.content:
            result = self.interpreter.run(line)
            results.append(result)
            print(result)

    def _hibernate(self):
        pass
