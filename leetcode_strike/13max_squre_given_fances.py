# 1. Brute force

m=6
n=8
hfences=[2,5,6]
vfences=[2,4]

# like we have give the m*n matrix and their is only vfences and hfences so we can remove lhis only.


# add the last and first number

vfences.insert(0,1)
vfences.append(m)


hfences.insert(0,1)
hfences.append(n)


# sort them
vfences.sort()
hfences.sort()

print(vfences)
print(hfences)

height=set()
      
# find the all possible heights
for i in range(len(vfences)-1):
    for j in range(i+1,len(vfences)):
        height.add(vfences[j]-vfences[i])

# print(height)
maxi=-1
for i in range(len(hfences)-1):
    
    for j in range(i+1,len(hfences)):
        if hfences[j]-hfences[i] in height:
            maxi=max(maxi,(hfences[j]-hfences[i])**2)

print(maxi)
