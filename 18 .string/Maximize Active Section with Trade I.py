class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        cnt = 1
        group = []

        for i in range(1,len(t)):

            if t[i] == t[i-1]:
                cnt += 1
            else:
                group.append((t[i-1],cnt))
                cnt = 1

        group.append((t[-1],cnt))
        one = s.count('1')
        ans = one


        for i in range(1,len(group) -1) :
            if group[i][0] == '1'and group[i-1][0] =='0' and group[i+1][0] =='0':
                gain = group[i-1][1] + group[i+1][1]
                ans = max(ans,gain+one)

        return ans

# time and space complexity is O(n)