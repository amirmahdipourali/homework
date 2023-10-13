def Make_a_Fraction(numerator,denominator):
    fraction={'n':numerator,'d':denominator}
    return fraction
def show_fraction(fraction):
    print("",fraction["n"],"\n ----\n" , fraction["d"]) 
def sum_fraction(pair1,pair2):
    Fraction = {}
    Fraction["n"] = (pair1["n"] * pair2["d"]) + (pair2["n"] * pair1["n"])
    Fraction["d"] = pair1["d"] * pair2["d"]
    return Fraction
def sub_fraction(pair1,pair2):
    Fraction = {}
    Fraction["n"] = (pair1["n"] * pair2["d"]) - (pair2["n"] * pair1["n"])
    Fraction["d"] = pair1["d"] * pair2["d"]
    return Fraction
def mul_fraction(pair1, pair2):
    Fraction = {}
    Fraction["s"] = pair1["s"] * pair2["s"] 
    Fraction["m"] = pair1["m"] * pair2["m"] 
    return Fraction
def div_fraction(pair1, pair2):
    Fraction = {}
    Fraction["s"] = pair1["s"] * pair2["m"] 
    Fraction["m"] = pair1["m"] * pair2["s"] 
    return Fraction
print('1.sum')
print('2.sub')
print('3.mul')
print('4.div')
op=(input('what is your operetor: '))
numerator1 = float(input("enter your first numerator: "))
denominator1 = float(input("enter your first denominator: "))
numerator2 = float(input("enter your second numerator: "))
denominator2 = float(input("enter your second denominator: "))
Fraction1 = Make_a_Fraction(numerator1, denominator1)
Fraction2 = Make_a_Fraction(numerator2, denominator2)
if op == '1':
    answer=sum_fraction(Fraction1,Fraction2)
    show_fraction(answer)
elif op == '2' :
    answer=sub_fraction(Fraction1,Fraction2)
    show_fraction(answer)
elif op == '3' :
    answer=mul_fraction(Fraction1,Fraction2)
    show_fraction(answer)
elif  op == '4' :
    answer=div_fraction(Fraction1,Fraction2)
    show_fraction(answer)
else:
    print('something is wrong')