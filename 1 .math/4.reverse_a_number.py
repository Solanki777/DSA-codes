# using string conversion
class Solution:
    def reverse(self, x: int) -> int:

        temp=str(abs(x))
        temp=temp[::-1]
        temp=int(temp)

        # constrain
        if temp < -2**31 or temp > 2**31 - 1:
            return 0

        if x<0:
            return -temp
        else:
            return temp
        
# time and space complexity is O(log x)
        
# mathemetically
class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        sign=-1 if x<0 else 1
        ans=0

        

        while temp>0:
            last_bit=temp%10
            ans=ans*10+last_bit
            temp=temp//10
        
        ans*=sign
        return 0 if ans<-2**31 or ans>2**31-1 else ans

# time complexity is O(logn) and space complexity is O(1)