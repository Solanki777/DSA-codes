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

    def remove(self):
        if self.head is None:
            print("empty list")
            return
        curr=self.head

        while curr is not None and curr.next is not None:
            nex=curr.next
            while nex is not None and curr.value==nex.value:
                curr.next=nex.next
                if nex.next is not None:
                    nex.next.prev=curr
                nex=nex.next

            curr=curr.next






dl=Doubly()
# dl.travers()
dl.insert_at_head(9)
dl.insert_at_head(6)
dl.insert_at_head(6)
dl.insert_at_head(6)
dl.insert_at_head(1)
dl.insert_at_head(1)
dl.insert_at_head(1)
dl.remove()
dl.travers()