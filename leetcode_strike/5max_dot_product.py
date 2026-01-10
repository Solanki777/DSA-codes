def maxDotProduct(nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [[-float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                # Four choices:
                # 1. Take current product and add to previous best (dp[i-1][j-1])
                # 2. Start fresh with just current product
                # 3. Skip nums1[i-1] (dp[i-1][j])
                # 4. Skip nums2[j-1] (dp[i][j-1])
                dp[i][j] = max(
                    prod + max(dp[i - 1][j - 1], 0),  # add to previous or start fresh
                    dp[i - 1][j],
                    dp[i][j - 1],
                    prod  # in case all previous are negative and this is positive
                )
        
        return dp[m][n]
nums1=[2,-1,-2,4]
nums2=[-3,3,-2]
print(maxDotProduct(nums1,nums2))