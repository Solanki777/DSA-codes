
source = "abcdefgh"
target = "acdeeghh"
original = ["bcd", "fgh", "thh"]
changed = ["cde", "thh", "ghh"]
cost = [1, 3, 5]

sl = Solution()
print(sl.minimumCost(source, target, original, changed, cost))
