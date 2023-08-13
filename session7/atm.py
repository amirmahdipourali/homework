#amirs pasword = 648860
password=648860
conter=0
while conter != 3:
    p=int(input("enter your password: "))
    conter+=1
    if p!=password:
        print ("try agine")
        continue
    elif p==password:
        print("wlcome")
        break
print("you are lookd out")
