class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            if ch in pairs:  # closing bracket
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:  # opening bracket
                stack.append(ch)

        return len(stack) == 0

# time complexity and space complexity is O(n)