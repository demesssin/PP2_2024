from datetime import datetime, timedelta

date1 = datetime.now()
date2 = date1 + timedelta(days=12)

seconds_difference = (date2 - date1).total_seconds()

print("Difference in seconds between first date and second date is:", seconds_difference)