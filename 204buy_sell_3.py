# pure recursion with time complexity of O(2^n) and space complexity of(n)
class Solution:
    def recursion(self, index, tra, prices, c_buy):
        if index==len(prices):
            return 0
        if tra==2:
            return prices[index]
        
        if c_buy==1:
            buy=-prices[index]+self.recursion(index+1,tra,prices,0)
            not_buy=self.recursion(index+1,tra,prices,1)
            profit=max(buy, not_buy)
            
        else:
            sell=prices[index] + self.recursion(index+1, tra+1 , prices, 1)
            not_sell=self.recursion(index+1, tra , prices, 0)
            profit=max(sell,not_sell)

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.recursion(0,0,prices,1)
        