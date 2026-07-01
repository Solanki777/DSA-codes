from collections import deque
class Solution:
    def bfs(self, adj):
        visted=[0]*len(adj)
        result=[]

        queue=deque([0])
        visted[0]=1
        while queue:
            node=queue.popleft()
            result.append(node)

            for n in adj[node]:
                    if visted[n]==0:
                        visted[n]=1
                        queue.append(n)
        return result

# time complexity is O(v+E) and space complexity is O(v)