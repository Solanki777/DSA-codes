def get_ans(nums):
    s=set()
    for i in range(len(nums)):
        if nums[i] in s:
            return nums[i]
        s.add(nums[i])
nums=[5,1,5,2,3,5,4]
print(get_ans(nums))