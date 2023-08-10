saf=['ahmad','milad','ashkan','mohahd','said','daryosh']
conter=0
while conter<3 :
    name=(input("what is your name: "))
    x=len(saf)
    j=int(input("where do you want to be: "))
    j-=1
    conter+=1
    saf.insert(j,name)
print(saf)
