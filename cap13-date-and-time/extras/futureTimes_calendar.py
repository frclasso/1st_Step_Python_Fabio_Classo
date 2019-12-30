#!/usr/bin/env python3

# Calculating future times
from datetime import datetime, timedelta
now = datetime.now()

twoDays = now + timedelta(days=2)

treeWeeksAgo = now - timedelta(weeks=3)

print(f'Daqui a dois dias:{twoDays.date()}')

print(f"Tree weeks ago: {treeWeeksAgo.date()}")

print()


# Using calendar library
import calendar

cal = calendar.month(2018,10)  # October 2001
print(cal)

cal2 = calendar.weekday(2018, 10, 24)  # What's 11 weekday
print(cal2)


