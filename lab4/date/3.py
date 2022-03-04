# Write a Python program to drop microseconds from datetime.

from datetime import datetime, timedelta

print("datetime without microseconds")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))