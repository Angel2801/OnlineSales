import json
from datetime import datetime


class LogReader:
    def __init__(self):
        self.__filepath = "./logs/log_data.json"
        self.logs = self.__readLogs(self.__filepath)
        self.buffer = []
        self.__sortLogs()

    def __readLogs(self, filepath):
        # Open and load the JSON file
        with open(filepath, "r") as file:
            logs = json.load(file)
        return logs

    def displayLogs(self):
        # Display each log in the buffer
        for log in self.buffer:
            print(log)

    def __getLogs(self):
        # Print the logs to understand the structure
        print("Logs loaded from file:")
        print(self.logs)

        # Iterate through each dictionary in the list
        for log_collection in self.logs:
            # Each log_collection is a dictionary of logs keyed by microservice names
            for microservice_name, log_details in log_collection.items():
                try:
                    # Print log details to help with debugging
                    print("Processing log entry:", log_details)

                    # Parse the date and time into a datetime object
                    date_time_str = f"{log_details['date']} {
                        log_details['time']}"
                    parsed_datetime = datetime.strptime(
                        date_time_str, "%a %B %d %Y %H:%M:%S %Z"
                    )

                    # Separate date and time
                    log_date = parsed_datetime.date()
                    log_time = parsed_datetime.time()

                    transformed_log = {
                        "date": log_date,  # Store date part separately
                        "time": log_time,  # Store time part separately
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
        # Sort the buffer by the 'date' and 'time' fields
        self.buffer.sort(key=lambda x: (x["date"], x["time"]))