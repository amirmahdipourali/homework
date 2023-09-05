number=int(input('Enter the diameter of the rhombus: '))
for i in range(number):
    print((number - i) * ' ', end='')
    print((i*2) * '◭')
for j in range(number,0,-1):
    print((number - j) * ' ', end='')
    print((j*2)*'◭')