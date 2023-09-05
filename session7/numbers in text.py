text=(input("enter a text: "))
list=["1","2","3","4","5","6","7","8","9","0"]
new_sum=0
for i in text :
   if i in list:
       sum=int(i)
       new_sum=sum+new_sum
   else :
       continue
print(new_sum)