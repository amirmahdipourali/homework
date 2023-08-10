un1="hamid133"
ps1=12345
un2="mamad shepesh"
ps2=3567849
un3="s.a.i.d"
ps3=20588
un4="omid gameing"
ps4=986542
un5="taleby"
ps5=915633842
username=(input("plaese enter your username:"))
password=int(input("plaese enter your password:"))
if username == un1 and password == ps1:
    print("hi",un1,"you are good to go")
elif username == un2 and password == ps2:
    print("hi",un2," you are good to go")
elif username == un3 and password == ps3:
    print("hi",un3," you are good to go")
elif username == un4 and password == ps4:
    print("hi",un4," you are good to go")
elif username == un5 and password == ps5:
    print("hi",un5," you are good to go")
else:
    print("sory",username,"but something is wrong with your password")