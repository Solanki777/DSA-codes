import math

# count =0 
# num=23450980654

# while num>0:
#     count+=1
#     num=num//10 #it takes init value means floor value
#     print(num)
# print(count)

# other method using log

num=23450980654

flr=math.log(num,10)
flr=flr+1
result=math.floor(flr)
print(result)
