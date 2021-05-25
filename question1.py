from datetime import datetime

TOTAL_MINUTES = 24 * 60
def calculate_percentage():
    current_datetime = datetime.now()
    return ((current_datetime.hour * 60 + current_datetime.minute) / TOTAL_MINUTES) * 100

print(calculate_percentage())