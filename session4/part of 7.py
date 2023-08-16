num=int(input("what is your number : "))
if num % 7 == 0 :
    print ("yes")
else :
    while num % 7 != 0 :
        num += 1
    print("the next number that is equl to 7 is",num)