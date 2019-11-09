import calendar as cal
import datetime as dt
import random as r

current_date = dt.datetime.now()

year = current_date.year

month = current_date.month

text_calendar = cal.TextCalendar().formatmonth(
    theyear=year, themonth=month, w=7, l=0)


sets_reps = [("4", "10"), ("4", "15")]

work_1 = [" chest ", "  back ", "  shldrs ",
          " legs ", " stomach ", " arms "]

r.shuffle(work_1)

new_cal_arr = text_calendar.split("\n")[0:2]

new_cal_arr.append(" ".join(work_1) + "  rest")

new_cal = text_calendar.split("\n")[2:-1]

for i, week in enumerate(new_cal):

    if i < 3:
        workout = sets_reps[0]
    else:
        workout = sets_reps[1]
    if len(week) < 53:
        spaces = " " * (abs(len(week) - len(new_cal[2])) + 3)
        new_week = new_cal[i] + f"{spaces}{workout[0]}/{ workout[1]}"
    else:
        new_week = new_cal[i] + f"   {workout[0]}/{ workout[1]}"
    new_cal_arr.append(new_week)

with open("workout-calendar.txt", mode="w") as f:
    f.write("\n\n".join(new_cal_arr))
