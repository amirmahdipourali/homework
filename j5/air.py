print("c->k = 1 , c -> f = 2 , f-> k = 3 , f -> c = 4")
print("k-> c = 5 K-> F = 6")
a=(input("what do you want to do: "))
if (a=="1"):
    b=float(input("c=: "))
    f=float(b+273.15)
    print("your answer is",f)
elif (a=="2"):
    b=float(input("c=: "))
    f=float(b*1.8)+32
    print("your answer is",f)
elif (a=="3"):
    b=float(input("f=: "))
    f=(b-32)/1.8+273.15
    print("your answer is",f)
elif (a=="4"):
    b=float(input("f=: "))
    f=float(b-32)/1.8
    print("your answer is",f)
elif (a=="5"):
    b=float(input("k=: "))
    f=273.15-b
    print("your answer is",f)
elif (a=="6"):
    b=float(input("k=: "))
    f=459.67-(b*1.8)
    print("your answer is",f)
else:print("eeeeeee something went worng")