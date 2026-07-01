class Node:
    def __init__(self,val):
        self.value=val
        self.left=None
        self.right=None


drinks=Node("drinks")
cold=Node("cold")
hot=Node("hot")
pepsi=Node("pepsi")
wodka=Node("wodka")
chai=Node("chai")
coffee=Node("coffee")

# print(drinks) it will print the object address
drinks.left=cold
drinks.right=hot
cold.left=pepsi
cold.right=wodka
hot.left=chai
hot.right=coffee

print(drinks.right.value)        
print(drinks.right.left.value)        
print(drinks.left.value)
print(drinks.left.left.value)
