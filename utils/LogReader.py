import json
from datetime import datetime


class LogReader:
    def __init__(self):
        self.__filepath = "./logs/log_data.json"
        self.logs = self.__readLogs(self.__filepath)
        self.buffer = []
        self.__sortLogs()

    def __readLogs(self, filepath):
        with open(filepath, "r") as file:
            logs = json.load(file)
        return logs

    def displayLogs(self):
        for log in self.buffer:
            print(log)

    def __getLogs(self):
        for log_collection in self.logs:
            for microservice_name, log_details in log_collection.items():
                try:
                    time_str = log_details["time"].split(" ")[
                        0
                    ] 
                    date_time_str = f"{log_details['date']} {time_str}"
                    parsed_datetime = datetime.strptime(
                        date_time_str, "%a %B %d %Y %H:%M:%S"
                    )

                    log_date = parsed_datetime.date()
                    log_time = parsed_datetime.time()

                    transformed_log = {
                        "date": log_date,  
                        "time": log_time,  
                        "microservice_name": microservice_name,
                        "log_type": log_details["log_type"],
                    }
                    self.buffer.append(transformed_log)

                except KeyError as e:
                    print(f"Missing key in log entry: {e}")
                except ValueError as e:
                    print(f"Value error with log entry: {e}")

    def __sortLogs(self):
        self.__getLogs()
        self.buffer.sort(key=lambda x: (x["date"], x["time"]))

log_reader = LogReader()
log_reader.displayLogs()