class Queue():
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1

    def __repr__(self):
        return "-".join([str(i) for i in self.queue[self.front+1:self.rear+1]])
    
    def isEmpty(self):
        return self.front==self.rear
    
    def isFull(self):
        return self.front==self.size-1

    def enqueue(self,num):
        if self.isFull():
            print("Queue is full")
        else:
            self.rear+=1
            self.queue[self.rear]=num
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.front+=1

q=Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
q.dequeue()
print(q)