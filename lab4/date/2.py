# Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

print("yesterday: ", datetime.now() - timedelta(days=1))
print("today: ", datetime.now())
print("tomorrow: ", datetime.now() + timedelta(days=1))


