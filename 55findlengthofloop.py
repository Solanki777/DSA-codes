class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Sinlgy:
    def __init__(self):
        self.head=None

    def append(self,value):
        new_node=Node(value)
        curr=self.head

        # if linked list is empty
        if self.head==None:
            self.head=new_node
            return
        
        else:
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node


    def makecirc(self,data,loc_data):
        self.append(data)
        curr=self.head
        while curr.value!=loc_data:
            curr=curr.next
        addre=curr.next
        
        while curr.next is not None:
            curr=curr.next
        curr.next=addre
    # my method:Time:  O(n) (curr in arr is linear search) Space: O(n)
    # def find_circle(self):
    #     curr=self.head
    #     visited=[]
    #     while curr!=None:
    #         if curr in visited:
    #             print("cycke detected",curr.value)
    #             return
    #         visited.append(curr)
    #         curr=curr.next
    #     print("cycle not detected")

    # optimal solution(floyd's):time complexity is O(n) in worst case but space complexity is O(1)
  
    def find_length(self):
        slow=self.head
        fast=self.head
        l1=0
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=1
                fast=fast.next
                while slow!=fast:
                    fast=fast.next
                    count+=1
                return count
        return 0
            
            
            
# Time & Space Complexity
# Time: O(n)
# Space: O(1)
ssl=Sinlgy()
ssl.append(5)
ssl.append(9)
ssl.append(1)
ssl.append(7)
ssl.append(6)
ssl.append(4)
ssl.append(9)
ssl.append(2)
ssl.makecirc(8,1)

# 5 → 9 → 1 → 7 → 6 → 4 → 9 → 2 → 8
#             ↑                     ↓
#             ← ← ← ← ← ← ← ← ← ← ←

print(ssl.find_length())
# ⏱ Time & Space Complexity

# Time: O(n)

# Space: O(1)
        