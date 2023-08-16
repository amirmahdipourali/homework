word=(input("enter a word: "))
if word == "A":
    nam=word.lower()
else:
    nam=word.upper()
conter=0
list=[]
for i in range(5):
    name=(input("enter a name: "))
    new_number=name.capitalize()
    if word in new_number :
        conter+=1
        list.append(new_number)
    elif nam in new_number :
        conter+=1
        list.append(new_number)
print(list)
print(conter)
