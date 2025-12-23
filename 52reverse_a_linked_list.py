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
            
    # # my method:time and space complexity is O(N)
    # def reverse(self):
        
    #     # for empty list
    #     if self.head==None :
    #         return
        
    #     # if head only
    #     if self.head.next==None:
    #         return self.head
        
    #     temp=[]
    #     curr=self.head
    #     while curr!=None:
    #         temp.append(curr.value)
    #         curr=curr.next

    #     print(temp)
        
    #     curr=self.head
    #     count=len(temp)-1
    #     while curr!=None:
    #         curr.value=temp[count]
    #         count-=1
    #         curr=curr.next
    #     return self.head.value

    # optimal time complexity is O(N) and space complexity is O(1)

    def reverse(self):
        curr=self.head
        prev=None
        
        while curr is not None:
            up=curr.next
            curr.next=prev
            prev=curr
            curr=up
        return prev


ssl=Sinlgy()
ssl.append(10)
ssl.append(20)
ssl.append(40)
ssl.insertat(0,1)
ssl.insertat(3,30)
ssl.travers()
ssl.delateat(1)
ssl.delateat(30)
ssl.travers()
print("head is : ",ssl.reverse())
ssl.travers()
        


        