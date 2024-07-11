import os

from src.settings import Settings

class Date:
    def __init__(self, settings: Settings):
       self.settings: Settings = settings

    def check(self, date: list):
        results: dict = {}

        if (len(date) == self.settings.format.size):
            for item in date:
                results = self._run_tests(item)

        return results

    def _run_tests(self, item: str):
        command: function = None
        tests: dict = {
            "range": {
                "command": self._is_range,
                "result": False
            },
            "enumeration": {
                "command": self._is_enumeration,
                "result": False
            },
            "number": {
                "command": self._is_number,
                "result": False
            }
        }

        for test in tests.keys():
            command = tests[test]["command"]
            tests[test]["result"] = command(item)

        return tests

    def _is_number(self, element: str):
        return (element.isnumeric())

    def _is_range(self, element: str):
        return ('-' in element)

    def _is_enumeration(self, element: str):
        return (',' in element)

class Checker:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self.date: Date = Date(self.settings)

    def check_date(self, date: list):
        return self.date.check(date)

class Result:
    def __init__(self):
        self.date: list = []

class Interpreter:
    def __init__(self, settings: Settings):
        self.settings: Settings = settings
        self.result: Result = Result()
        self.checker: Checker = Checker(self.settings)

    def run(self, line: str):
        date: list = self._extract_date(line)
        command: str = self._extract_command(line)
        results: dict = {
            "date": self.checker.check_date(date)
        }
        
        return results

    def _extract_date(self, content: str):
        date: list = content.split(' ')[:-1]
        
        return date

    def _extract_command(self, content: str):
        command: str = content.split(' ')[-1]

        return command
