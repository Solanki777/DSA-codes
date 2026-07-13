# TIme complexity and space complexity is O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        c = "123456789"
        res = []

        for i in range(9):
            for j in range(i,9):
                curr = c[i:j+1]

                if low<=int(curr)<=high:
                    res.append(int(curr))
        
        res.sort()
        return res


            
           