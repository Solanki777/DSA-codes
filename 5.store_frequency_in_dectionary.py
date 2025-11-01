# let we have list nums=[5,3,8,2,4,6,8,5,5,2,1,0,0,2,6,5,9,7]

# so we have to create dictiory that have unique values and each value stores the frequncy from the above list called nums
# like dict={  5:4,
#     3:1}
# 
# Method 1:
nums=[5,3,8,2,4,6,8,5,5,2,1,0,0,2,6,5,9,7]
freq_map=dict()

# empty dictionary is mad by using 
# freq_map=dict() or freq_map={}

for el in range(0,len(nums)):
    if (nums[el]) in freq_map:
        freq_map[nums[el]]+=1
        
    else:
        freq_map[nums[el]]=1
print(freq_map)


# method2:
# do you know freq_map.get(5,0)?
# =>it means it find the 5 character data into the dictionary if it exits than it will return the value of 5 else it returns 0

nums=[5,3,8,2,4,6,8,5,5,2,1,0,0,2,6,5,9,7]
freq_map={}

for el in range(0,len(nums)):
    freq_map[nums[el]]=freq_map.get(nums[el],0)+1
print(freq_map)
