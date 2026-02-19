# deque is class in python which very similar with doubly linked list . Deque take O(1) time complexity is most of the cases so it is some effician

from collections import deque

lit=deque()
lit.append(100)
lit.append(200)
lit.append(300)
lit.appendleft(400)
lit.appendleft(500)

print (lit)
lit.popleft()
lit.pop()
print (lit)
