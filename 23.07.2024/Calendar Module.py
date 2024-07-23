#  https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true

import calendar
month,day,year=map(int,input().split())
day_of_week=calendar.weekday(year,month,day)
day=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(day[day_of_week])
