import json

# Data to be written into JSON
log_data = [
    {
        "micro-service-a1": {'log_type': 'INFO', 'date': 'Wed July 24 2023', 'time': '12:30:00 GMT+0530'},
        "micro-service-c1": {'log_type': 'ERROR', 'date': 'Wed July 24 2023', 'time': '12:40:00 GMT+0530'},
        "micro-service-c2": {'log_type': 'DEBUG', 'date': 'Wed July 24 2023', 'time': '12:35:00 GMT+0530'},
        "micro-service-d1": {'log_type': 'ERROR', 'date': 'Wed July 24 2023', 'time': '12:20:00 GMT+0530'},
        "micro-service-b2": {'log_type': 'INFO', 'date': 'Wed July 24 2023', 'time': '12:45:00 GMT+0530'},
        "micro-service-b2": {'log_type': 'DEBUG', 'date': 'Wed July 24 2023', 'time': '12:50:00 GMT+0530'},
        "micro-service-z2": {'log_type': 'ERROR', 'date': 'Wed July 24 2023', 'time': '12:55:00 GMT+0530'},
        "micro-service-g2": {'log_type': 'ERROR', 'date': 'Wed July 24 2023', 'time': '12:52:00 GMT+0530'},
        "micro-service-d1": {'log_type': 'DEBUG', 'date': 'Wed July 24 2023', 'time': '12:48:00 GMT+0530'}
    }
]
json_file_path = '/Users/angelkanjiya/Angel/OnlineSales/logs/log_data.json'
with open(json_file_path, 'w') as file:
    json.dump(log_data, file, indent=4)
