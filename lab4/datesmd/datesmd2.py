from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

print("Yesterday was:", yesterday.strftime('%d of %B, %A'))
print("Today is:", today.strftime('%d of %B , %A'))
print("Tomorrow will be:", tomorrow.strftime('%d of %B , %A'))
