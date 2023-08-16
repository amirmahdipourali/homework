list=['homa','sara','amir mahdi','pooria','sara','shahriyar','atefeh','sara','ali','sina','sara','sara','navid reza','sadra']
c=list.count('sara')
list.sort()
while 'sara' in list:
    list.remove('sara')
print(c)
print(list)