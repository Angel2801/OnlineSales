import json


class LogReader:
    def __init__(self):
        self.__filepath = "./logs/log_data.json"
        self.logs = self.__readLogs(self.__filepath)

    def __readLogs(self, filepath):
        with open(filepath, "r") as file:
            logs = json.load(file)
        return logs

    def displayLogs(self):
        for log in self.logs:
            print(log)