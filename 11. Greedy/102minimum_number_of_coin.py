class Solution:
    def findMin(self, n):
        currency=[10,5,2,1]
        coin=0

        for cur in currency:
            coin+=n//cur
            n=n%cur

        return coin
    
# time complexity is O(len(currency))
            

      
       