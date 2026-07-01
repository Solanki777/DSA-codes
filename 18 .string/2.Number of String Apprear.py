class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count=0
        for ch in patterns:
            if ch in word:
                count+=1
        return count
       

# time compelxity is O (len(patterns) * O(word)) and space complexity is O(1)