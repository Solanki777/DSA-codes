# brute force solution time complexity is O(nlogn) and space complexity is O(n)
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if coins<cost:
                break
            count+=1
            coins-=cost
        return count

# recursion solution : time complexity is O(2^n) and space complexity is O(n)
class Solution:
    def recurison(self,costs,index,coins):
        if index==len(costs):
            return 0
        
        buy=0
        if coins>=costs[index]:
            buy=1+self.recurison(costs,index+1,coins-costs[index])
        not_buy=self.recurison(costs,index+1,coins)

        return max(buy,not_buy)        

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return self.recurison(costs,0,coins)

        