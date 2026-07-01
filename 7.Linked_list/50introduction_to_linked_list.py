# linked list is collection of data storing value within the index in non-contiguous manner not like list.A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer. The way they are linked together is that each node points to where in the memory the next node is placed.

# why linked list used rather than list ?

# assume you opened many tabs in single browser like tab1-tab2-tab3-tab4 if we store this in list . than if i want delete any tab than the sift their position which is not sufficient so we have to use linked list. it's easy to add or delete new tab in linked list than list in non-contingous manner

# 1.sigly linked list:we can only travers in one direction that's why it's called singly.

# class node:
#     def __init__(self,value):
#         self.val=value
#         self.next=None
        
# node1=node(5)
# node2=node(34)
# node3=node(23)
# node4=node(13)

# node1.next=node2
# node2.next=node3
# node3.next=node4

# # this is object which gives address
# print(node1)
# print(node1.val)

# # address of next node2 object
# print(node1.next)


# singly linkedlist operation
# first we learn basic operation like append and travers

class Node:
    def __init__(self,val):
        self.value=val
        self.next=None

class Sinlgy:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        curr=self.head
        if self.head is None:
            self.head=new_node
        else:
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

    def insert_at(self,data,position):
        new_node=Node(data)
        new_node.next=None
        curr=self.head
        pre_node=None
        count=0

        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            while count<position and curr is not None:
                pre_node=curr
                curr=curr.next
                count+=1
            pre_node.next=new_node
            new_node.next=curr

    def delete(self,data):
        temp=self.head
        # case1:empty list
        if self.head==None:
            print("empty SSL")
            return
        
        # case2:head  to be deleted
        if temp.value==data:
            self.head=temp.next
            return
        
        # case3 : search the node
        prev=None
        while temp is not None:
            if temp.value==data:
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next

        # case 4: not not found
        print("node not found")
        
        
    def traverse(self):
        if self.head is None:
            print("SSL is empty")
        
        else:
            curr=self.head
            while curr is not None:
                print(curr.value,end=" ")
                curr=curr.next
            print("None")

ssl = Sinlgy()
ssl.traverse()
ssl.append(10)
ssl.traverse()
ssl.append(20)
ssl.append(30)
ssl.append(40)
ssl.traverse()
        
# | Operation          | Time Complexity | Space Complexity |
# | ------------------ | --------------- | ---------------- |
# | Append             | `O(n)`          | `O(1)`           |
# | Insert at head     | `O(1)`          | `O(1)`           |
# | Insert at position | `O(n)`          | `O(1)`           |
# | Delete by value    | `O(n)`          | `O(1)`           |
# | Traverse           | `O(n)`          | `O(1)`           |
# | Search             | `O(n)`          | `O(1)`           |



