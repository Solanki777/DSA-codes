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
            
    
    def travers(self):
        curr=self.head
        if self.head==None:
            print("linked list is empty")
            return
        else:
            while curr!=None:
                print(curr.value,end=" ")
                curr=curr.next

            print("None")
    
    
    # bruteforce
    # def removefromlast(self,delete):

    #     if self.head==None:
    #         print("list is empty")
    #         return
        
    #     # if node is alone
    #     if self.head.next==None and delete==1:
    #         self.head=None
    #         return
        
    #     # count the position of total elements in linked list
    #     curr=self.head
    #     t=0

    #     while curr!=None:
    #         curr=curr.next
    #         t+=1

    #     count=t-delete

    #     # if deletin node is head
    #     if count==0:
    #         self.head=self.head.next
    #         return

    #     if count<0:
    #         print("Invalid node not do be deleted")
    #         return    

    #     prev=None
    #     curr=self.head
    #     t=1

    #     while t!=count+1:
    #         prev=curr
    #         curr=curr.next
    #         t+=1
        
    #     prev.next=curr.next
    
    # optimal
    def removefromlast(self,delete):
        
        # empty list
        if self.head==None:
            print("list is empty")
            return
        
        slow=self.head
        fast=self.head

        for _ in range(delete):
            if fast is None:
                print ("invalid position")
                return
            fast=fast.next

        if fast==None:
            self.head=self.head.next
            return self.head.value
        
        while fast.next is not None:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next
        return self.head

        
ssl=Sinlgy()
ssl.append(1)
ssl.append(2)
ssl.append(3)
ssl.append(4)
ssl.append(5)
ssl.append(6)
print(ssl.removefromlast(6))
ssl.travers()
        


        