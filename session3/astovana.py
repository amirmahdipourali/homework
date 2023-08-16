h=float(input("enter h :"))
r=float(input("enter r :"))
import math
v=r*r*h*(math.pi)
mj=h*r*2*(math.pi)
m=mj+2*(v/h)
print("your area is",m)
print("your lateral area is",mj)
print("and your volume is",v)