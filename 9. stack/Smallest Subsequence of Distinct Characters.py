class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        stack = []

        for index,character in enumerate(s): last[character] = index

        for index, character in enumerate(s):

            if character in stack : continue

            while stack and stack[-1] > character  and index < last[stack[-1]]: stack.pop()
            stack.append(character)
        
        return "".join(stack)

# Time complexity is O(n*k) where k is uniq characters and space complexity is O(k) 