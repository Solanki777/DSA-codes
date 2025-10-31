import math
from math import sqrt
# factors like for 10 =[1,2,5,10]
#                   11 =[1,11]

# num=int(input("enter a number:"))
# i=1
# divisior=[]
# while (i<=num):
#         if num%i==0:
#                 divisior.append(i)
#         i+=1

# print(divisior)
                
# for 20=[1,2,4,5,10,20] here always loop runs to half of the number because after 10 we can not find any factor about 20 so we go till half way and we know the number is itself if factor

# Best Way

num=int(input("enter a number:"))
i=1
divisior=[]
while (i<=num//2):
        if num%i==0:
                divisior.append(i)
        i+=1
divisior.append(num)
print(divisior)

# Time complexity=O(N) for both cases in best way time complexity is O(N/2) but constatn removed and space complexity is O(K) where k is number of elements in divisor[]

# optimal solution
# if we divide 26 by 2 than the answer is 13 then 2 and 13 both are divior so for 36:
#            1-36
#            2-18
#            3-12
#            4-9
#            6-6
# all are getted here we have to not go for half way we have to go till root of 36=6 so this is optimal solution . Solution not gives in order answer but it is optimal
        
num=int(input("enter a number:"))
divisior=[]
i=1
while (i<=int(sqrt(num))):
        if num%i==0:
                divisior.append(i)
                if num//i!=i:
                        divisior.append(num//i) #6-6
                        
                
        i+=1

print(divisior)
# time complexity is O(n^1/2) +O(nlogn)[if sort the answer]
# space complexity is O(divisior)
