num = int(input("enter your number: "))

divisors = []
for i in range(1, num):
    if (num % i) == 0:
        divisors.append(i)

if sum(divisors) == num:
    print(num," number is number")
else:
    print(num," is not whole number")
    