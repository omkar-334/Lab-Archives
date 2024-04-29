class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
    def __repr__(self):
        return self.data

class DoubleLL:
    def __init__(self):
        self.head=None

    def __repr__(self):
        node = self.head
        output=""
        while node is not None:
            output+=str(node.data)+"<->"
            node = node.next
        return output+"None"

    def isEmpty(self):
        if self.head is None:
            print("Linked list is empty")
            return True
        return False

    def reverse(self):
        curr = self.head

        while curr is not None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev

        if temp is not None:
            self.head = temp.prev

    def add_first(self,num):
        node=Node(num)
        node.next=self.head
        node.prev=None
        if self.head is not None:
            self.head.prev=node
        self.head=node

    def add_last(self,num):
        node=Node(num)
        curr=self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=node
        node.prev=curr

    def remove(self,num):
        curr=self.head

        if self.isEmpty():
            return

        while curr.data!=num:
            if curr is None:
                print("node not found in linked list")
                return
            curr=curr.next
        curr.prev.next=curr.next
        curr.next.prev=curr.prev

dll=DoubleLL()
dll.add_first(5)
dll.add_first(6)
dll.add_first(7)
dll.add_last(4)
print(dll)
dll.remove(6)
print(dll)
dll.reverse()
print(dll)