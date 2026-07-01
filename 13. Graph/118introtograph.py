# 1. What is graph ?
# A graph is a collection of:

# Vertices/node (V) → nodes (points)
# Edges (E) → connections between nodes

# 2.Types of Graphs

#   1.Undirected Graph
#    Connection is two-way
#     Example: A — B (you can go both ways)

#    2.Directed Graph (Digraph)
#     One-way connection
#     Example: A → B (only from A to B)

#    3.Weighted Graph
#     Edges have values (cost, distance, time)

#    4.Unweighted Graph
#     No cost on edges


# 4. A cycle is a path in a graph where:

#     You start from a node
#     Travel through edges
#     And come back to the same node
#     Without repeating edges (in simple terms)

# 5.  Path:A sequence of vertices where each adjacent pair is connected by an edge.
#  If a path starts and ends at the same vertex, then it is a cycle
# (with one condition):
# 👉 No vertex should be repeated (except the first/last one)

# 6. Degree in graph: degree(node) means number of nodes's are connected with particular node. like degree(1) means how many other node are connected with 1

# total degree= 2 * Edges

# 7. indegree(node):incomming edges
# 8. outdegree(node): outgoing edges
