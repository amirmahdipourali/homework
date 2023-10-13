def set_time(time):
    dict=time.split(":")
    time={ "h": int(dict[0]),"m": int(dict[1]),"s": int(dict[2])}
    return time
def check_time(time):
    while not(0 < time["s"] < 60 and 0 < time["m"] < 60):
        if time["s"] > 60:
            time["s"] -= 60
            time["m"] += 1
        elif time["s"] < 0:
            time["m"] -= 1
            time["s"] += 60 
        if time["m"] > 60:
            time["m"] -= 60
            time["h"] += 1
        elif time["m"] < 0:
            time["h"] -= 1
            time["m"] += 60

    return time

def sum_of_date(time1, time2):
    time = {"h": time1["h"] + time2["h"] , "m": time1["m"] + time2["m"] , "s": time1["s"] + time2["s"] }
    time = check_time(time)
    return time
def sub_of_date(time1, time2):
    time = {"h": time1["h"] - time2["h"] , "m": time1["m"] - time2["m"] , "s": time1["s"] - time2["s"] }
    time = check_time(time)
    return time

def show_time(time):
    print(f"{time['h']}:{time['m']}:{time['s']}")
print('1.sum')
print('2.sub')
op=(input('what is your operetor: '))
pair1=(input('enter your first time frame like so (h:m:s) : '))
pair2=(input('enter your second time frame like so (h:m:s) : '))
pair1=set_time(pair1)
pair2=set_time(pair2)
if op == '1':
    answer=sum_of_date(pair1,pair2)
    show_time(answer)
elif op == '2':
    answer=sub_of_date(pair1,pair2)
    show_time(answer)