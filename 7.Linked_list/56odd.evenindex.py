# here we have given a linked list we have to make it like first put odd indexed nodes than even indexed noeds in sequnce order

# index => 0-1-2-3-4-5-6
# list  => 8-7-1-5-6-4-9-None

# ans:
# list=>8-1-6-9-7-5-4-None
# return 8

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

    def insertat(self,position,data):
        new_node=Node(data)
        curr=self.head
        prev_node=None
        count=0

        if position==0:
            new_node.next=self.head
            self.head=new_node
            return

        else:
            while curr!=None and count<position:
                prev_node=curr
                curr=curr.next
                count+=1

            if count!=position:
                print("position not found")
                return
            
            prev_node.next=new_node
            new_node.next=curr
 


    def delateat(self,data):

        # linkedlist empty
        if self.head==None:
            print("linkedlist is empty")
            return
        
        # first node
        if self.head.value==data:
            self.head=self.head.next
            return
        
        curr=self.head
        pre_node=None
        found=False

        while curr!=None:
            if curr.value==data:
                found=True
                break
            else:
                pre_node=curr
                curr=curr.next

        if found:
            pre_node.next=curr.next
        
        else:
            print("not found")
    #     my method:Time Complexity: O(n) and Space Complexity: O(n)
    # def oddeven(self):
    #     count=1
    #     curr=self.head
    #     odd=[]
    #     even=[]
    #     while curr!=None:
    #         if count%2!=0:
    #             odd.append(curr.value)
    #         else:
    #             even.append(curr.value)
    #         curr=curr.next
    #         count+=1
    #     print(odd)
    #     print(even)
    #     curr=self.head
    #     for el in odd :
    #         curr.value=el
    #         curr=curr.next
    #     for el in even:
    #         curr.value=el
    #         curr=curr.next

    #   my method:Time Complexity: O(n) and Space Complexity: O(1)
    def oddeven(self):
        if self.head is None or self.head.next is None:
            return 
        temp=self.head
        odd=self.head
        even=self.head.next
        head=even
        
        while even!=None and even.next!=None:
            odd.next=odd.next.next
            odd=odd.next

            even.next=even.next.next
            even=even.next
        odd.next=head
        return temp






            


ssl=Sinlgy()
ssl.append(8)
ssl.append(7)
ssl.append(1)
ssl.append(5)
ssl.append(6)
ssl.append(4)
ssl.append(9)
ssl.travers()
print(ssl.oddeven())
ssl.travers()
        


        