fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
print(fruits)
#index , shows the block of your name in a list from 0

#insert , you can put a str in list a block of your chosing
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1,"me")
print(fruits)
#copy,copys your list
cars=["bmw","volvo","ford"]
x=cars.copy()
print(x)
#
cars.extend(fruits)
print(cars)