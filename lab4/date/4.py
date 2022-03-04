# Write a Python program to calculate two date difference in seconds.

from datetime import datetime, timedelta

date1 = datetime.now()
date2 = datetime(2021, 6, 1, 23, 30, 30)
difference = date1 - date2
print(difference.total_seconds())  