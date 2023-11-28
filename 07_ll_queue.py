class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def __repr__(self):
        node = self.front
        output=""
        while node is not None:
            output+=str(node.data)+"->"
            node = node.next
        return output+"None"

    def isEmpty(self):
        return self.front==self.rear

    def isFull(self):
        return self.front==self.size-1

    def enqueue(self,num):
        node=Node(num)
        if self.rear is None:
            self.front=node
            self.rear=node
            return
        self.rear.next=node
        self.rear=node

    def dequeue(self):
        if self.isEmpty():
            return
        self.front=self.front.next
        if self.front is None:
            self.rear=None

Q=Queue()
Q.enqueue(5)
Q.enqueue(8)
print(Q)
Q.enqueue(11)
print(Q)
Q.dequeue()
print(Q)



