import random
n=random.randint(0,100)
print(n)
a=(input("is this number biger or smaller then your number or is it the same ? : "))
list=[n,'b','c']
print(list)
while a != "same":

    if a=="b":
        n=list.pop(n)
        n=random.randint(n,100)
        print(n)
        list.append(n)
        a=(input("how abote now ?"))
    elif a=="s":
        n=list.pop(n)
        n=random.randint(0,n)
        list.append(n)
        print(n)
        a=(input("how abote now ?"))
print("lets play agein")