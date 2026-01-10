def sol(s1, s2):
    memo = {}

    def find(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # If s1 is exhausted, delete all remaining chars of s2
        if i >= len(s1):
            return sum(ord(c) for c in s2[j:])

        # If s2 is exhausted, delete all remaining chars of s1
        if j >= len(s2):
            return sum(ord(c) for c in s1[i:])

        # If characters match, move both pointers
        if s1[i] == s2[j]:
            ans = find(i + 1, j + 1)
        else:
            ans = min(
                ord(s1[i]) + find(i + 1, j),
                ord(s2[j]) + find(i, j + 1)
            )

        memo[(i, j)] = ans
        return ans

    return find(0, 0)


s1 = "eat"
s2 = "sea"
print(sol(s1, s2))
