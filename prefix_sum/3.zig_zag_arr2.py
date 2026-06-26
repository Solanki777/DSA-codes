# time complexity is O(items^3 * logn) (logn for matrix exponentiation)
# space complexity is O(items^2)

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        items = r - l + 1
        size = 2 * items

        # matrix multiplication
        def mul(a, b):
            rows = len(a)
            cols = len(b[0])
            mid = len(b)
            res = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for k in range(mid):
                    if a[i][k] == 0:
                        continue
                    val = a[i][k]
                    for j in range(cols):
                        res[i][j] = (res[i][j] + val * b[k][j]) % MOD
            return res

        # binary exponentiation
        def power(mat, exp):
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1

            while exp:
                if exp & 1:
                    res = mul(res, mat)
                mat = mul(mat, mat)
                exp >>= 1
            return res

        # transition matrix
        mat = [[0] * size for _ in range(size)]

        # states:
        # 0 ... items-1       -> DOWN
        # items ... 2*items-1 -> UP
        for i in range(items):
            # UP -> DOWN
            for j in range(i):
                mat[i][j + items] = 1

            # DOWN -> UP
            for j in range(i + 1, items):
                mat[i + items][j] = 1

        # initial vector
        dp = [[1] * size]

        # matrix exponentiation
        mat = power(mat, n - 1)

        # final answer
        ans = mul(dp, mat)
        return sum(ans[0]) % MOD