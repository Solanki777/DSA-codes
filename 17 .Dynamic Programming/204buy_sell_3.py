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
    
# dp + recursion time complexity is O(6n) and space complexity is O(n) + O(6n)
class Solution:
    def recursion(self, index, tra, prices, c_buy,dp):
        if index==len(prices):
            return 0

        if tra==2:
            return 0

        if dp[index][tra][c_buy]!=-1:
            return dp[index][tra][c_buy]
        
        if c_buy==1:
            buy=-prices[index]+self.recursion(index+1,tra,prices,0,dp)
            not_buy=self.recursion(index+1,tra,prices,1,dp)
            profit=max(buy, not_buy)
            
        else:
            sell=prices[index] + self.recursion(index+1, tra+1 , prices, 1,dp)
            not_sell=self.recursion(index+1, tra , prices, 0,dp)
            profit=max(sell,not_sell)

        dp[index][tra][c_buy]= profit
        return dp[index][tra][c_buy]

    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[-1,-1] for _ in range(3)] for _ in range(len(prices))]
        return self.recursion(0,0,prices,1,dp)

# tabulation time complexity and space complexity is O(6n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[0,0] for _ in range(4)] for _ in range(len(prices)+1)]

        for index in range(len(prices)-1,-1,-1):
            for tra in range(2):
                
                buy=-prices[index]+dp[index+1][tra][0]
                not_buy=dp[index+1][tra][1]
                dp[index][tra][1]=max(buy,not_buy)
                
            
                sell=prices[index] +dp[index+1][tra+1][1]
                not_sell=dp[index+1][tra][0]
                dp[index][tra][0]=max(sell,not_sell)

        return dp[0][0][1]
        
    
# space optimization 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ahed=[[0,0] for _ in range(3)]

        for index in range(len(prices)-1,-1,-1):
            curr=[[0,0] for _ in range(3)]
            for tra in range(2):
                
                buy=-prices[index]+ahed[tra][0]
                not_buy=ahed[tra][1]
                curr[tra][1]=max(buy,not_buy)
                
            
                sell=prices[index] +ahed[tra+1][1]
                not_sell=ahed[tra][0]
                curr[tra][0]=max(sell,not_sell)
            ahed=curr

        return ahed[0][1]

# further more space optimization 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1=float('-inf')
        sell1=0
        buy2=float('-inf')
        sell2=0

        for price in prices:
            buy1=max(buy1, -price)
            sell1=max(sell1, buy1 + price)

            buy2=max(buy2, sell1 - price)
            sell2=max(sell2, buy2 + price)

        return sell2