class Stack:
    def __init__(self,size):
        self.stack=[0]*size
        self.top=-1
        self.size=size

    def __repr__(self):
        return "-".join([str(i) for i in self.stack[:self.top+1]])

    def isEmpty(self):
        return self.top==-1

    def isFull(self):
        return (self.top+1)==self.size

    def push(self, num):
        if self.isFull():
            print("Stack is full")
        else:
            self.top+=1
            self.stack[self.top]=num

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.top-=1
            return self.stack[self.top+1]

    def peek(self):
        print(self.stack[self.top])


s=Stack(4)
s.push(1)
s.push(2)
s.push(3)
print(s)
s.pop()
print(s)

