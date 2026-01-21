nums=[2,3,5,7]
ans=[]

for i in range(len(nums)):
    if nums[i]==2:
        ans.append(-1)
    else:
        mask=~(((nums[i]+1)&~nums[i])>>1)
        ans.append(nums[i]&mask)
print(ans)
