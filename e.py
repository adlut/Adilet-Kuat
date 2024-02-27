from datetime import datetime

current_date = datetime.now()
date_without_microseconds = current_date.replace(microsecond=0)

print("Current Date:", current_date)
print("Date without Microseconds:", date_without_microseconds)
