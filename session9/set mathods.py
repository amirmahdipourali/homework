# add - remove - discard - update 
colors = {'blue','yellow','black','gray','yellow'}
print(colors)

colors.add('white')
print(colors)

colors.remove('yellow') 
print(colors)

colors.discard('blue')
print(colors)

names = {'ali','alireza','hoseyn'}
colors.update(names)
print(colors)
