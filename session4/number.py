a=float(input("enter your number: "))
if a % 10 > 6 and a % 2 == 0 and a >=0 :
    print("e")
elif a % 10 < 4 and a % 2 == 0 and a >=0 :
    print("b")
elif a <= 0 :
    print ("d")
else: 
    print("c")