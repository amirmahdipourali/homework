first_number=int(input('enter your first number: '))
second_number=int(input('enter your second number: '))
therd_number=int(input('enter your therd number: '))
new_number=(second_number**2)+(4*first_number*therd_number)
print('the value of discriminant is',new_number)
sol1=(-second_number+new_number**0.5/2*first_number)
sol2=(+second_number+new_number**0.5/2*first_number)
print('the roots of this quadratic equation are',sol1,'and',sol2)