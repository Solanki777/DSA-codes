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

    def insert_at_loc(self,pos,value):
        new_node=Node(value)

        # empty list with inserting at head
        if pos==0:
            self.insert_at_head(value)
            return
        
        curr=self.head
        count=0

        while curr and count<pos-1:
            curr=curr.next
            count+=1
        
        if curr is None:
            print("index out of bound")
            return
        
        next_node=curr.next
        
        new_node.prev=curr
        new_node.next=next_node
        curr.next=new_node
        
        if next_node:
            next_node.prev=new_node

    def delete_at_head(self):

        # empty list
        if self.head is None:
            print("empty linkde list")
            return
        
        # single Node
        if self.head.next is None:
            self.head=None
            return
        
        self.head=self.head.next
        self.head.prev=None

    def delete_at_last(self):

        # empty list
        if self.head is None:
            print("empty list")
            return
        
        # only one node
        if self.head.next is None:
            self.head=None
            return 
        
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.prev.next=None
        
    def delete_at_loc(self,pos):

        if self.head is None:
            print("empty list")
            return
        
        if pos==0:
            self.delete_at_head()
            return 

        curr=self.head
        count=0

        while curr and count<pos:
            curr=curr.next
            count+=1

        if curr is None:
                print("index out of bound")
                return


        if curr.next is None:
            curr.prev.next=None
            return
        
        curr.prev.next=curr.next
        curr.next.prev=curr.prev


        

        


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




dl=Doubly()
# dl.travers()
dl.insert_at_head(1)
dl.insert_at_head(2)
dl.insert_at_head(3)
dl.insert_at_loc(0,9)
dl.delete_at_head()
dl.delete_at_last()
dl.travers()