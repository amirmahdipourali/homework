def is_prime(number):
    x=[]
    for i in range(1,number+1):
        if number % i == 0:
            x.append(i)
    if len(x) == 2:
        return 'prime'
    else :
        return 'not prime'
print(is_prime(7))