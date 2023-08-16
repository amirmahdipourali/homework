num=(input("what is your number: "))
b=0
c=0
b += num.count("0")
b += num.count("2")
b += num.count("6")
b += num.count("4")
b += num.count("8")
c += num.count("1")
c += num.count("1")
c += num.count("1")
c += num.count("1")
c += num.count("1")
if c>b:
    print("there are more even numbers")
elif c<b:
    print("there are more odd numbers")