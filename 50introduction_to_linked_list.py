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
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

    def travers(self):
        if not self.head:
            print("SLL is empty")

        else:
            curr=self.head
            while curr is not None:
                print(curr.value,end=" ")
                curr=curr.next
            print()


sll=Sinlgy()
sll.append(12)
sll.append(115)
sll.append(124)
sll.append(18)
sll.travers()


