import calendar as cal
import datetime as dt
from random import random, shuffle


current_date = dt.datetime.now()

year = current_date.year

month = current_date.month

class text_calendar():
    """
    Creates a workout calendar with strings. writes a new file to print out
    args:
        sets_reps(optional): takes an array of two tuples, the first will be set for the first
            half of the month and the second for the last. default is [("4", "10"), ("4", "15")]

        workouts(optional):
        takes a list of 6 different workouts
        default [" chst  ", " back  ", " shdrs  ", " legs  ", " stmch  ", " arms "]
    """


    def __init__(self, sets_reps=[("4", "10"), ("4", "15")], workouts=[" chst  ", " back  ", " shdrs  ",
                        " legs  ", " stmch  ", " arms  "]):
        self.text_calendar = cal.TextCalendar().formatmonth(
            theyear=year, themonth=month, w=7, l=0)
        self.sets_reps = sets_reps
        self.work_1 = workouts
        shuffle(self.work_1)
        self.new_cal_top = self.text_calendar.split("\n")[:1]
        self.double_work_list = self.work_lst(self.work_1)
        self.create_headings()
        self.new_cal = self.text_calendar.split("\n")[2:-1]


    def work_lst(self, wrk_list):
        new_lst = [item for item in wrk_list]
        shuffle(wrk_list)
        new_lst_2 = [item for item in wrk_list]
        return [new_lst, new_lst_2]

    


    # pick two random workouts per day and append it to the top of the cal 
    def create_headings(self):
        self.new_cal_top.append(" ".join(self.double_work_list[0]))
        self.new_cal_top.append(" ".join(self.double_work_list[1]) + "  rest")
        self.new_cal_top.append("_" *60)
        self.new_cal_top.append(" ".join(self.text_calendar.split("\n")[1:2]))


    
    def build_weeks(self):
        for i, week in enumerate(self.new_cal):

            if i < 3:
                workout = self.sets_reps[0]
            else:
                workout = self.sets_reps[1]
            if len(week) < 53:
                spaces = " " * (abs(len(week) - len(self.new_cal[2])) + 3)
                new_week = self.new_cal[i] + f"{spaces}{workout[0]}/{ workout[1]}"
            else:
                new_week = self.new_cal[i] + f"   {workout[0]}/{ workout[1]}"
            self.new_cal_top.append(new_week)

    def create_calendar(self):
        with open("workout-calendar.txt", mode="w") as f:
            f.write("\n".join(self.new_cal_top))
