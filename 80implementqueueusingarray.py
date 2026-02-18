class myQueue:
    def __init__(self, n):
        self.arry = []
        self.size = n   # maximum capacity of queue

    def isEmpty(self):
        return len(self.arry) == 0

    def isFull(self):
        return len(self.arry) == self.size

    def enqueue(self, x):
        if self.isFull():
            print("Queue is Full! Cannot enqueue:", x)
            return -1
        self.arry.append(x)
        print(x, "enqueued")
        return 0

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! Cannot dequeue")
            return -1
        removed = self.arry.pop(0)
        print(removed, "dequeued")
        return removed

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arry[0]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arry[-1]


# 🔹 Creating Queue of size 3
q = myQueue(3)

# 🔹 Calling isEmpty()
print("Is Queue Empty?", q.isEmpty())   # True

# 🔹 Calling enqueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# 🔹 Calling isFull()
print("Is Queue Full?", q.isFull())     # True

# 🔹 Calling getFront()
print("Front Element:", q.getFront())

# 🔹 Calling getRear()
print("Rear Element:", q.getRear())

# 🔹 Calling dequeue()
q.dequeue()

# 🔹 State after one dequeue
print("Front after dequeue:", q.getFront())
print("Rear after dequeue:", q.getRear())

# 🔹 Enqueue again
q.enqueue(40)

# 🔹 Final queue operations
print("Final Queue Front:", q.getFront())
print("Final Queue Rear:", q.getRear())
print("Is Queue Empty?", q.isEmpty())
print("Is Queue Full?", q.isFull())
