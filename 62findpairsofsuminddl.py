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

    # bruteforce solution time complexity is O(n²)
    # def sum(self,key):
    #     curr=self.head
    #     arr=[]
    #     while curr is not None:
    #         n=curr.next
    #         while n is not None:
    #             if (curr.value+n.value)==key:
    #                 arr.append([curr.value,n.value])
    #             n=n.next
    #         curr=curr.next
    #     return arr

    # better solution:time complexity is O(n) and space complexity is O(n)
    # def sum(self,key):
    #     curr=self.head
    #     arr=set()
    #     ans=[]
    #     while curr is not None:
    #         arr.add(curr.value)
    #         curr=curr.next

    #     for el in arr:
    #         temp=key-el
    #         if temp in arr and el<temp:
    #             ans.append([el,temp])
    #     return ans

    # optimal solution:Time: O(n) and Space: O(1)
    def sum(self,key):
        right=self.head
        left=self.head
        arr=[]
        while right.next is not None:
            right=right.next

        while right.value>left.value:
            ans=right.value+left.value
            if (ans)==key:
                arr.append([left.value,right.value])
                right=right.prev
                left=left.next
            elif ans>key:
                right=right.prev
            else:
                left=left.next
        return arr


            







dl=Doubly()
# dl.travers()
dl.insert_at_head(9)
dl.insert_at_head(8)
dl.insert_at_head(7)
dl.insert_at_head(6)
dl.insert_at_head(5)
dl.insert_at_head(4)
dl.insert_at_head(3)
dl.insert_at_head(2)
dl.insert_at_head(1)
dl.travers()

print(dl.sum(7))