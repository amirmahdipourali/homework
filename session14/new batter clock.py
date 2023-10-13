class colck:
    def __init__(self,h,m,s,h2,m2,s2):
        self.h = h
        self.m = m
        self.s = s
        self.h2 = h2
        self.m2 = m2
        self.s2 = s2
    def sum(self):
        hours = self.h + self.h2
        minutes = self.m + self.m2
        seconds = self.s + self.s2
        while not(0 < seconds < 60 and 0 < minutes < 60):
            if seconds >= 60:
                seconds -= ((seconds // 60) * 60)
                minutes += (seconds // 60)
            if minutes >= 60:
                minutes -= ((minutes // 60) * 60)
                hours += (minutes // 60)
        print(str(hours) + ":" + str(minutes)  + ":" + str(seconds))
    def sub(self):
        hours = self.h - self.h2
        minutes = self.m - self.h2
        seconds = self.s - self.h2
        while not(0 <= seconds <= 60 and 0 <= minutes <= 60):
            if second < 0:
                minut -= 1
                second += 60
            if minut < 0:
                hour -= 1
                minut += 60
        print(str(hours) + ":" + str(minutes)  + ":" + str(seconds))
t = input("enter time1:for exampel (20:45:30)\n")
t2 = input("enter time2:for exampel (20:45:30)\n")
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
t = t.split(":")
t = [eval(i) for i in t]
t2 = t2.split(":")
t2 = [eval(i) for i in t2]
time = colck(t[0], t[1], t[2], t2[0], t2[1], t2[2])
if op == 1:
    time.sub()
else:
    time.sum()