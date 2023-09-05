def GCD(num1, num2):
    if num2 == 0:
        return num1
    else:
        return GCD(num2, num1 % num2)
print(GCD(5,6))