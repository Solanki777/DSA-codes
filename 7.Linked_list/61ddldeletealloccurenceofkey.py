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
    
    def delteocc(self,key):

        # if linked list is empty
        if self.head is None:
            print("thir is no list")
            return
       
        curr=self.head
        
        while curr is not None:
            next_node=curr.next

            if curr.value==key:

                # for head
                if curr==self.head:
                    self.head=next_node
                    if self.head is not None:
                        self.head.prev=None



                # for tail
                elif curr.next is None:
                    curr.prev.next=None

                # for middle
                else:
                    curr.prev.next=next_node
                    next_node.prev=curr.prev
            curr=next_node
        return self.head
                    



dl=Doubly()
# dl.travers()
dl.insert_at_head(2)
dl.insert_at_head(1)
dl.insert_at_head(3)
dl.insert_at_head(2)
dl.insert_at_head(2)
dl.travers()
print(dl.delteocc(2))
dl.travers()