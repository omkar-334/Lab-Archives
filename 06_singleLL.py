class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

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

    def add_first(self, num):
        node=Node(num)
        node.next = self.head
        self.head = node
    
    def add_last(self, num):
        node=Node(num)
        curr=self.head
        if curr is None:
            curr = node
            return
        while curr.next is not None:
            curr=curr.next
        curr.next=node

    def add_before(self,target,num):
        node=Node(num)
        curr=self.head

        if self.isEmpty():
            return
        if curr.data==target:
            return self.add_first(num)
        while curr.data!=target:
            if curr.next is None:
                print("node not found in linked list")
                return
            prev=curr
            curr=curr.next
        prev.next=node
        node.next=curr

    def add_after(self,target,num):
        node=Node(num)
        curr=self.head

        if self.isEmpty():
            return
        while curr.data!=target:
            if curr is None:
                print("node not found in linked list")
                return
            curr=curr.next
        if curr.next is None:
            return self.add_last(num)
        next=curr.next
        curr.next=node
        node.next=next

    def remove(self,num):
        curr=self.head
        if self.isEmpty():
            return
        while curr.data!=num:
            if curr is None:
                print("node not found in linked list")
                return
            prev=curr
            curr=curr.next
        prev.next=curr.next


node1=Node(0)
node2=Node(1)
node3=Node(2)
ll=LinkedList()
ll.head=node1
node1.next=node2
node2.next=node3
ll.add_first(99)
ll.add_last(87)
print(ll)
ll.add_before(99,5)
ll.add_before(3,100)
print(ll)
ll.add_after(87,13)
ll.add_after(5,10)
print(ll)
ll.remove(10)
ll.remove(0)
print(ll)