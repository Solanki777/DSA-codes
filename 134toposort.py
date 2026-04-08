# step 1: iterate each one non visited 
# step 2: make it visited
# step 3: find non visited nodes from it's surrounding of current node
# step 4: after completing dfs put the current node in stack
#step 5: if thre is deadend then make it 2 so it means there is no further way to go

class Solution:
    def topoSort(self, V, edges):
        visited=[0 for _ in range(V)]
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)


        stack=[]

        def dfs(node):
            visited[node]=1
            
            for neg in adj[node]:
                if visited[neg]==0:
                    if dfs(neg):
                        return True
                elif visited[neg]==1:
                    return True
            
            
            stack.append(node)
            visited[node]=2
            return False
            


        for i in range(V):
            if visited[i]==0:
                if dfs(i):
                    return []
        return stack[::-1]
    
# time complexity and space complexity  is O(v+e)