
   
class Solution:
    def dfs(self, adj):
        vis=[0]*len(adj)
        ans=[]
        
        def solve(adj,node):
            vis[node]=1
            ans.append(node)
            for i in (adj[node]):
                if vis[i]==0:
                    solve(adj,i)
        
        solve(adj,0)
        return ans

# space complexity is O(v) and time  complexity is O(V + E)
