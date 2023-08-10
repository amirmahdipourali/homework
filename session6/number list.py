conter=0
list=[]
while conter < 5 :
    number=(input("enter 5 numbers: "))
    conter+=1
    list.append(number)
list.sort()
print(list)
list.reverse()
print(list)