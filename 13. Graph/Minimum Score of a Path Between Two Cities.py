# time and space complexity is O(V + E)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        # adjlist
        adjlist=[[] for _ in range(n+1)]
        ans=float('inf')

        for u,v,w in roads:
            adjlist[u].append((v,w))
            adjlist[v].append((u,w))
            
        visited=[False]*(n+1)
        queue=[1]

        while queue:
            node=queue.pop()
            visited[node]=True

            for neg , w in adjlist[node]:
                if not visited[neg]:
                    queue.append(neg)
                    ans=min(ans,w) 
        return ans
                
                 