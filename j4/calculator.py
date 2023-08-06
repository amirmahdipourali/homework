print ('1=+')
print ("2=-")
print ("3=x")
print ("4=÷")
print ("5=x²")
print ("power to itself")
print ("6=√")
print ("7=sin(Degree)")
print ("8=cos(Degree)")
print ("9=tan(Degree)")
print ("10=cot(Degree)")
print ("11=rond numbers")
print ("12=sell")
print ("log")
import math
op=(input("enter the operator:"))
if (op=="1") or (op=='+'):
   a=(input("enter a:"))
   b=(input("enter b:"))
   answer=a+b
   print(answer)
elif (op=="2") or (op=="-"):
   a=(input("enter a:"))
   b=(input("enter b:"))
   answer=a-b
   print(answer)
elif (op=="3") or (op=="x"):
   a=(input("enter a:"))
   b=(input("enter b:"))
   answer=a*b
   print(answer)
elif (op=="4") or (op=="/"):
   a=(input("enter a:"))
   b=(input("enter b:"))
   answer=a/b
   print(answer)
elif (op=="5") or (op=="**"):
   a=(input("enter a:"))
   b=(input("enter b:"))
   answer =(math.pow(a,b))
   print(answer)
