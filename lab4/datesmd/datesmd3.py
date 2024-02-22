from datetime import datetime

current_date = datetime.now()

date_without_microseconds = current_date.replace(microsecond=0)

print("Original datetime:", current_date)
print("Datetime without microseconds:", date_without_microseconds)
