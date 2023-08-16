number=(input("enter your number: "))
list=[]
for i in range(number):
    list.append(i)
new_list = "*".join(list)
print(new_list)