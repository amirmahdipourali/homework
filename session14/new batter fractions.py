def vacuum_chamber(numerator, denumerator):
    vacuum_number = {"numbers": numerator, "dnum": denumerator}
    return vacuum_number

class fractions:
    def __init__(self, dict1 , dict2):
        # Properties
        self.dict1 = dict1
        self.dict2 = dict2

    # Methods
    def mul(self):
        result_num = self.dict1["numbers"] * self.dict2["numbers"]
        result_dnum = self.dict1['dnum'] * self.dict2['dnum']
        return result_num , result_dnum
    def sub(self):
        result_num = (self.dict1["numbers"] * self.dict2['dnum']) - (self.dict2["numbers"] * self.dict1['dnum'])
        result_dnum = self.dict1['dnum'] * self.dict2['dnum']
        return result_num , result_dnum
    def sum(self):
        result_num = (self.dict1["numbers"] * self.dict2['dnum']) + (self.dict2["numbers"] * self.dict1['dnum'])
        result_dnum = self.dict1['dnum'] * self.dict2['dnum']
        return result_num , result_dnum
    def div(self):
        if not(self.dict2['dnum'] == 0 or self.dict2["numbers"] == 0):
            result_num = self.dict1["numbers"] * self.dict2['dnum']
            result_dnum = self.dict1['dnum'] * self.dict2["numbers"]
            return result_num , result_dnum
        else:
            return "Your second fraction is undefined because it has a zero denominator"
op = int(input("1.sum\n2.sub\n3.mul\n4.div\n yoer nenter number of operation: "))
eqp1 = {}
eqp2 = {}
for i in range (1, 3):
    numbers = int(input(f"enter numerator{i}: "))
    denum = int(input(f"enter denumerator{i}: "))
    if i == 1:
        eqp1  = vacuum_chamber(numbers, denum)
    else:
        eqd2 = vacuum_chamber(numbers, denum)
d = fractions(eqp1, eqp2)
if op == 1:
    a , b = d.sum()
    print(a, "\n-----\n", b)
elif op == 2:
    a , b = d.sub()
    print(a, "\n-----\n", b)
elif op == 3:
    a , b = d.mul()
    print(a, "\n-----\n", b)
elif op == 4:
    try:
        a , b = d.div()
        print(a, "\n-----\n", b)
    except:
        print(d.div(eqp1, eqp2))