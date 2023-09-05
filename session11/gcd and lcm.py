import math
def gcd(first_number,second_number):
#    answer=math.gcd(x,y)
    x=[]
    y=[]
    result=[]
    for i in range(1,first_number+1):
        if first_number % i == 0:
            x.append(i)
    for i in range(1,second_number+1):
        if second_number % i == 0:
            y.append(i)
    for j in y:
        for i in x:
            if j == i:
                result.append(i)
    gcd = result[len(result)-1]  
    return gcd

def lcm(x,y):
#    answer=math.lcm(x,y)
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            answer = greater  
            break
        greater+=1
    return answer
print(lcm(6,15))
print(gcd(6,15))