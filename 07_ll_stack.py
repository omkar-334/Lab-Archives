class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data

class Stack:
    def __init__(self):
        self.head=None

    def __repr__(self):
        node = self.head
        output=""
        while node is not None:
            output+=str(node.data)+"->"
            node = node.next
        return output+"None"

    def isEmpty(self):
        if self.head is None:
            print("Linked list is empty")
            return True
        return False

    def push(self,num):
        node=Node(num)
        node.next=self.head
        self.head=node

    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp=self.head
            self.head=self.head.next
            temp.next=None
            return temp.data

    def peek(self):
        if self.isEmpty():
            return None
        else:
            print(self.head.data)


S=Stack()
S.push(2)
S.push(4)
S.push(5)
print(S)
S.pop()
print(S)
S.pop()
print(S)
