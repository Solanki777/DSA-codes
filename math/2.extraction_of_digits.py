class Solution:
    def extraction(self,number):
        ans=0
        while number>0:
            ans=number%10
            print(ans)
            number=number//10



# time complexity is O(logbase10(n)) becuase number is interger not string and space complexity is O(1)