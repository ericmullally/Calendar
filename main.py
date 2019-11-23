import calendar as cal
import datetime as dt
from random import random, shuffle

current_date = dt.datetime.now()

year = current_date.year

month = current_date.month

text_calendar = cal.TextCalendar().formatmonth(
    theyear=year, themonth=month, w=7, l=0)


sets_reps = [("4", "10"), ("4", "15")]

work_1 = [" chst  ", " back  ", " shdrs  ",
          " legs  ", " stmch  ", " arms  "]

          
shuffle(work_1)
def work_lst(wrk_list):
    new_lst = [item for item in wrk_list]
    shuffle(wrk_list)
    new_lst_2 = [item for item in wrk_list]
    return [new_lst, new_lst_2]

new_cal_top = text_calendar.split("\n")[:1]


# pick two random workouts and append it to the top of the cal 
double_work_list = work_lst(work_1)
new_cal_top.append(" ".join(double_work_list[0]))
new_cal_top.append(" ".join(double_work_list[1]) + "  rest")
new_cal_top.append("_" *60)
new_cal_top.append(" ".join(text_calendar.split("\n")[1:2]))


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
    new_cal_top.append(new_week)


with open("workout-calendar.txt", mode="w") as f:
    f.write("\n".join(new_cal_top))
