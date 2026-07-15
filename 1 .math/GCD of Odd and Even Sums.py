class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0
        count_odd = 1
        count_even = 2

        for _ in range(n):
            sum_odd += count_odd
            count_odd += 2

            sum_even += count_even
            count_even += 2
        
        # O(logn)
        while sum_even:
            sum_odd, sum_even = sum_even, sum_odd % sum_even

        return sum_odd


# Time complexity is O(n) and space complexity is O(1)

from math import gcd
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0
        count_odd = 1
        count_even = 2

        for _ in range(n):
            sum_odd += count_odd
            count_odd += 2

            sum_even += count_even
            count_even += 2

        return gcd(sum_odd,sum_even)