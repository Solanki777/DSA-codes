
# pure_recursion  time complexity is O(n^2) and space complexity is O(n)
class Solution:
    def recursion(self,index,can_b,prices):
        if index==len(prices):
            return 0
        
        if can_b==1:
            buy=-prices[index]+self.recursion(index+1,0,prices)
            not_buy=self.recursion(index+1,1,prices)
            profit=max(buy,not_buy)

        else:
            sell=prices[index]+self.recursion(index+1,1,prices)
            not_sell=self.recursion(index+1,0,prices)
            profit=max(sell,not_sell)
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.recursion(0,1,prices)
        