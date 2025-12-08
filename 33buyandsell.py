# bruteforce solution
# def find(nums):
#     max1=0
#     maxi=0
#     for b in range(len(nums)):
#         for s in range(b+1,len(nums)):
#             max1=nums[s]-nums[b]
#             maxi=max(maxi,max1)
#     if maxi<0:
#         return 0
#     else:
#         return maxi

# price=[7,2,1,5,6,4,8]
# ans=find(price)
# print(ans)

# here the time compelxity is O(n^2) and space compexity is O(1)

# optimal soution (Kadane's style)

def find(nums):
    max_profit=0
    mini_price=float("inf")
    for price in nums:
        mini_price=min(mini_price,price)
        max_profit=max(max_profit,price-mini_price)
    return max_profit

price=[7,2,1,5,6,4,8]
ans=find(price)
print(ans)

# time complexity is O(n) and space complexity is O(10)