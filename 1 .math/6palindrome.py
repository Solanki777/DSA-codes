class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp=0
        ans=x
        while x>0:
            temp=temp*10+(x%10)
            x=x//10
        return temp==ans

# Time complexity is O(logn) and space complexity is O(1)