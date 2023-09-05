def is_prime(number):
    x=[]
    for i in range(1,number+1):
        if number % i == 0:
            x.append(i)
    if len(x) == 2:
        return 'prime'
    else :
        return 'not prime'
lower_number =int(input("enter the lower number: "))
higher_number=int(input("enter the higher number: ")) 
prime=[]
for i in range(lower_number,higher_number+1):
    play=is_prime(i)
    if play == 'prime':
        prime.append(i)
    else:
        pass
print(prime)