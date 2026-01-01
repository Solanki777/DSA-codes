class Node:
    def __init__(self,val):
        self.value=val
        self.next=None
        self.prev=None

class Doubly:
    def __init__(self):
        self.head=None

    def insert_at_head(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node

    def travers(self):
        if self.head is None:
            print("empty list")
            return
        
        else:
            curr=self.head
            while curr is not None:
                print(curr.value,end=" ")
                curr=curr.next

            print("None")

    # time complexity is O(n) and space complexity is O(1)
    def revrse(self):

        if self.head is None:
            print("empty list")
            return

        curr=self.head

        while curr is not None:
            curr.next,curr.prev=curr.prev,curr.next
            if curr.prev is None:
                self.head=curr
            curr=curr.prev
       


dl=Doubly()
# dl.travers()
dl.insert_at_head(1)
dl.insert_at_head(2)
dl.insert_at_head(3)
dl.insert_at_head(4)
dl.insert_at_head(5)
dl.travers()
dl.revrse()
dl.travers()