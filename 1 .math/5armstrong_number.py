
# here they give armst=3 that why i use it 
# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. 

# Input: n = 372
# Output: false
# Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. 

class Solution:
    def armstrongNumber (self, n):
        ans=0
        check=n

        while n>0:
            last_digit=n%10
            ans+=last_digit**3
            n=n//10

        return check==ans

# time complexity is O(logn) and space complexity is O(1)