print("hi chack out your body mass index or bmi you can be any of the 4 thips")
print("underweight , overweight")
print("extremely obese , obese")
w=float(input("enter your weight in ks: "))
h=float(input("enter your heigt in cms: "))
h=h/100
bmi=w/(h*h)
if 18.5>bmi :
    print("underweight")
elif 24.9>bmi>18.5 :
    print("normal")
elif 29.9>bmi>25:
    print("overweight")
elif 34.9>bmi>30 :
    print("obese")
elif bmi>35 :
    print("extremely obese")