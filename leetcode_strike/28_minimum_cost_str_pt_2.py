from collections import defaultdict
import heapq

class Solution(object):

    # TLE promblem
    def __init__(self):
        self.dij_cache={}
    
    # dijkastra 
    def dijkast(self,srcsub,trgsub,adjlis):

        # if there is similar solution which is exites than go for it 
        if (srcsub,trgsub) in self.dij_cache:
            return self.dij_cache[(srcsub,trgsub)]
        

        dist=defaultdict(lambda:float('inf'))
        dist[srcsub]=0
        min_heap=[(0,srcsub)]

        while min_heap:

            curr_dist,curr_node=heapq.heappop(min_heap)

            if curr_dist>dist[curr_node]:
                continue

            for v,w in adjlis[curr_node]:
                new_dist=curr_dist+w
                if new_dist <dist[v]:
                    heapq.heappush(min_heap,(new_dist,v))
                    dist[v]=new_dist
        self.dij_cache[(srcsub,trgsub)]=dist[trgsub]
        return dist[trgsub]
    
    # solving 
    def solve(self,i,source,target,original,changed,cost,dp,adjlis,validlength):

        # if i reaches to last index retu zero 
        if i==len(source):
            return 0
         
        # if dp has similar solution than go for it 
        if dp[i]!=-1:
            return dp[i]
        
        # first cost is infinite defined
        result=float('inf')
        # if characters are same than not do anything increase the index than find the next solution
        if source[i]==target[i]:
            result=min(result,self.solve(i+1,source,target,original,changed,cost,dp,adjlis,validlength))
            
        # we tak only valid length strings only as substring
        for length in validlength:
            # if i reaches at position their no substring is posible
            if i+length > len(source):
                break
            
            # define the substrings
            srcsub=source[i:i+length]
            trgsub=target[i:i+length]
            
            # if substring has no cost to convert into target string then skip it 
            if srcsub not in adjlis:
                continue
            
            # find the sortes path usign dijkastra
            pathcost=self.dijkast(srcsub,trgsub,adjlis)

            # if there is no path skip it 
            if pathcost==float('inf'):
                continue
            
            # compare current result and other result 
            result=min(result,pathcost+self.solve(i+length,source,target,original,changed,cost,dp,adjlis,validlength))
        
        # store result 
        dp[i]=result
        
        # return the result 
        return result


    def minimumCost(self, source, target, original, changed, cost):

        # define the dp 
        dp=[-1] * (len(source)+1)

        # adjlist
        adjlis=defaultdict(list)
        
        # fill the adjlist 
        for el in range(len(original)):
            adjlis[original[el]].append((changed[el],cost[el]))
        
        # use set to ignore duplicates which can cause TLE 
        validlength=set()
         
        # fill it 
        for el in original:
            validlength.add(len(el))
        
        # sort it 
        validlength=sorted(validlength)
        
        
        ans=self.solve(0,source,target,original,changed,cost,dp,adjlis,validlength)
        return -1 if ans==float('inf') else ans

# improved version
# import heapq
# from collections import defaultdict

# class Solution:
#     def minimumCost(self, source, target, original, changed, cost):

#         BIG = float('inf')
#         n = len(source)

#         # ---------- build graph ----------
#         adj = defaultdict(list)
#         valid_lengths = set()

#         for o, c, w in zip(original, changed, cost):
#             adj[o].append((c, w))
#             valid_lengths.add(len(o))

#         valid_lengths = sorted(valid_lengths)

#         # ---------- dijkstra cache ----------
#         dijk_cache = {}

#         def dijkstra(start, end):
#             if (start, end) in dijk_cache:
#                 return dijk_cache[(start, end)]

#             pq = [(0, start)]
#             dist = {start: 0}

#             while pq:
#                 cost_u, u = heapq.heappop(pq)
#                 if u == end:
#                     break

#                 for v, w in adj.get(u, []):
#                     new_cost = cost_u + w
#                     if v not in dist or new_cost < dist[v]:
#                         dist[v] = new_cost
#                         heapq.heappush(pq, (new_cost, v))

#             ans = dist.get(end, BIG)
#             dijk_cache[(start, end)] = ans
#             return ans

#         # ---------- dp ----------
#         dp = [-1] * (n + 1)

#         def solve(i):
#             if i == n:
#                 return 0
#             if dp[i] != -1:
#                 return dp[i]

#             res = BIG

#             # same character
#             if source[i] == target[i]:
#                 res = solve(i + 1)

#             # substring replacement
#             for L in valid_lengths:
#                 if i + L > n:
#                     break

#                 s1 = source[i:i + L]
#                 s2 = target[i:i + L]

#                 if s1 not in adj:
#                     continue

#                 c = dijkstra(s1, s2)
#                 if c != BIG:
#                     res = min(res, c + solve(i + L))

#             dp[i] = res
#             return res

#         ans = solve(0)
#         return -1 if ans == BIG else ans

source = "abcdefgh"
target = "acdeeghh"
original = ["bcd", "fgh", "thh"]
changed = ["cde", "thh", "ghh"]
cost = [1, 3, 5]

sl = Solution()
print(sl.minimumCost(source, target, original, changed, cost))
