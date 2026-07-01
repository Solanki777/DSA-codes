#User function template for Python

# here we give adjacency matrix is give we have to travers through the mid node to calculate the minimum distance of all the node . Since the algorithm used to find the shortest path with all node to all node 

class Solution:
	def floydWarshall(self, dist):
		for via in range(len(dist)):
			for i in range(len(dist)):
				for j in range(len(dist)):
					if dist[i][via]!=10**8 and dist[via][j]!=10**8:
						dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
		return dist

# Time complexity is O(n^3) and O(1) space complexity

# How should you know the graph contains loop here 
# first you know that 0-->0 distance is 0 here when you traverse via the node like you 0-->3-->0 and both are negative weight than answer of 0-->0 becomes negative so we found the cycle 