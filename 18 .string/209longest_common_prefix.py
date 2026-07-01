
# time complexity is O(m*n) and space complexity is O(1)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]

        # find the minimum length from the characters in string
        min_string=strs[0]
        for char in strs:
            if len(min_string)>len(char):
                min_string=char
        
        
        for i in range(len(min_string)):
            for char in strs:
                if char[i]!=min_string[i]:
                    return min_string[:i]

        return min_string
    