# Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta

print(datetime.now())
print(datetime.now() - timedelta(days=5))


