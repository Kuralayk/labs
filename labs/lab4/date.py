#1
from datetime import datetime, timedelta
current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date: ", current_date.strftime("%Y-%m-%d"))
print("5 days ago: ", new_date.strftime("%Y-%m-%d"))

#2
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday: ",yesterday.strftime("%Y-%m-%d"))
print("Today: ",today.strftime("%Y-%m-%d"))
print("Tomorrow: ",tomorrow.strftime("%Y-%m-%d"))

#3
now = datetime.now()
time = now.replace(microsecond=0)
print("Date: ", time)

#4
date1 = datetime(2025, 2 , 9, 14, 30, 0)
date2 = datetime(2025, 2 , 7, 10, 15, 0)
diff = abs((date1 - date2).total_seconds())
print("result: ", diff)

