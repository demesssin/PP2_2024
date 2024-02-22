from datetime import datetime, timedelta

this_date = datetime.now()

old_date = this_date - timedelta(days=3, minutes= 12)

formatted_date = old_date.strftime('%Y-%m-%d-%H-%M')

print("Current Date:", this_date.strftime('%Y-%m-%d-%H-%M'))
print("Date five days ago:", formatted_date)
