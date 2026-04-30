# For max-heap we know that the parent is grater or eqal to childrean now we are getting replace some values inside the node by mainatinig the property of max-heap for that there is two operation:
#     1. heapify down : we putiing the elemnt . But the childrean are bigger than the parent which not follow the max-heap property. So we have to go down and put that new elemnt at it's appropriate place.
#     2. heapify Up: Here the new element is putted where the parent is smaller than new element so now we have to traverse on up side to put new element at it's appropritate place.


# we have bfs traversed almost completed binary tree is given in arr. also we given the ind where we have to put new element val. and heapify it to make tree correct
# max-heap tree 

class Solution:
    def heapifydown(self,arr,ind):

        largerel_ind=ind
        left_child=2*ind+1
        right_child=2*ind+2

        # left Child
        if left_child<len(arr) and arr[left_child]>arr[largerel_ind]:
            largerel_ind=left_child

        # right child 
        if right_child<len(arr) and arr[right_child]>arr[largerel_ind]:
            largerel_ind=right_child
        
        if largerel_ind!=ind:
            arr[largerel_ind],arr[ind]=arr[largerel_ind],arr[ind]
            self.heapifydown(arr,largerel_ind)
    
    def heapifyup(self,arr,ind):
        parent=(ind-1)//2
        if ind>0 and arr[parent]<arr[ind]:
            arr[parent],arr[ind]=arr[ind],arr[parent]
            self.heapifyup(arr,parent)



    def heapify(self,arr,ind,val):
        arr[ind]=val
        parent=(ind-1)//2
        if ind>0 and arr[ind]>arr[ind]>arr[parent]:
            self.heapifyup(arr,ind)
        else:
            self.heapifydown(arr,ind)

# Time complexity is O(logbase2N) and space coplexity is same for recursion stack space 