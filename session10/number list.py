duplicated_numbers=[]
repeaded_numbers={}
number_list=(input('give me a lot of numbers: '))

for i in number_list:
    if i not in duplicated_numbers:
        repeaded_numbers.update({i:0})
        duplicated_numbers.append(i)
    elif i in duplicated_numbers:
        repeaded_numbers[i] +=1
print(repeaded_numbers)
#print(duplicated_numbers)