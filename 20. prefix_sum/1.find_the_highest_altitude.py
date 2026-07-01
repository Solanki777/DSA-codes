class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=float('-inf')
        ans=0

        for alti in gain:
            ans+=alti
            maxi=max(maxi,ans)

        return maxi if maxi>0 else 0

# Time complexity is O(n) and space complexity is O(1)