num =int(input("Enter the number: "))
num2 =int(input("enter the number: ")) 
prime=[]
if num < num2:
    for i in range(num,num2):
        b=(i*2)-1
        prime.append(b)
elif num > num2:
        for i in range(num2,num):
            b=(i*2)-1
            prime.append(b)
print(prime)
