class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # it limits to 32 bit of 1 only

        while a:

            carry = ((a & b) << 1) & MASK
            b = (a ^ b) & MASK
            a = carry
        
        MAX = 0x7FFFFFFF

        if b> MAX : # this is negative number use 2's complement
            
            
            b = ~ (b ^ MASK)
        
        return b
