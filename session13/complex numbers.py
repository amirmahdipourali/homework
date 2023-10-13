num1_pair1 = float(input("enter your first number : "))
num2_pair1 = float(input("enter your second number  : "))
num1_pair2 = float(input("enter your first number : "))
num2_pair2 = float(input("enter your second number : "))
numbers = {"a1": num1_pair1, "b1": num2_pair1, "a2": num1_pair2, "b2": num2_pair2}
def sum(numbers):
    return f"{numbers['a1'] + numbers['a2']}, {numbers['b1'] + numbers['b2']}"
def sub(numbers):
    return f"{numbers['a1'] - numbers['a2']}, {numbers['b1'] - numbers['b2']}"
operation = int(input("""1 = sum
                + 2 = sub\n"""))

if operation == 1:
    print(sum(numbers))
elif operation == 2:
    print(sub(numbers))