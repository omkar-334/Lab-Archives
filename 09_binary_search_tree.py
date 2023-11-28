class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    # def __repr__(self):
        # lines = []
        # if self.right:
        #     found = False
        #     for line in repr(self.right).split("\n"):
        #         if line[0] != " ":
        #             found = True
        #             line = " ┌─" + line
        #         elif found:
        #             line = " | " + line
        #         else:
        #             line = "   " + line
        #         lines.append(line)
        # lines.append(str(self.value))
        # if self.left:
        #     found = False
        #     for line in repr(self.left).split("\n"):
        #         if line[0] != " ":
        #             found = True
        #             line = " └─" + line
        #         elif found:
        #             line = "   " + line
        #         else:
        #             line = " | " + line
        #         lines.append(line)
        # return "\n".join(lines)

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,num):
        if self.root is None:
            self.root=Node(num)
        else:
            self.recursive_insert(self.root,num)

    def recursive_insert(self,curr,num):
        if num<curr.value:
            if curr.left is None:
                curr.left=Node(num)
            else:
                self.recursive_insert(curr.left,num)
        elif num>curr.value:
            if curr.right is None:
                curr.right=Node(num)
            else:
                self.recursive_insert(curr.right,num)

    def search(self, value):
            return self.recursive_search(self.root, value)

    def recursive_search(self, curr, value):
        if curr is None or curr.value == value:
            return curr
        if value < curr.value:
            return self.recursive_search(curr.left, value)
        else:
            return self.recursive_search(curr.right, value)

    def delete(self, num):
        if self.root is None:
            return self.root
        else:
            self.recursive_delete(self.root,num)

    def recursive_delete(self,curr,num):
        if curr.value>num:
            curr.left = self.recursive_delete(curr.left, num)
            return curr
        elif curr.value < num:
            curr.right = self.recursive_delete(curr.right, num)
            return curr
        if curr.left is None:
            temp = curr.right
            del curr
            return temp
        elif curr.right is None:
            temp = curr.left
            del curr
            return temp
        else:
            succParent = curr
            succ = curr.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left
            if succParent != curr:
                succParent.left = succ.right
            else:
                succParent.right = succ.right
            curr.value = succ.value
            del succ
            return curr

    def inorder(self,Root):
        # left-root-right traversal
        if Root:
            self.inorder(Root.left)
            print(Root.value,end = ' ')
            self.inorder(Root.right)

    def postorder(self,Root):
        # left-right-root traversal
        if Root:
            self.postorder(Root.left)
            self.postorder(Root.right)
            print(Root.value, end=' ')

    def preorder(self,Root):
        # root-left-right traversal
        if Root:
            print(Root.value,end=" ")
            self.preorder(Root.left)
            self.preorder(Root.right)

    def __repr__(self):
        return self.recursive_display(self.root, "")

    def recursive_display(self,root, indent):
        if root:
            self.recursive_display(root.right, indent + "   ")
            print(indent + str(root.value))
            self.recursive_display(root.left, indent + "   ")
        return ""

bst=Tree()
bst.insert(8)
bst.insert(5)
bst.insert(6)
bst.insert(4)
bst.insert(11)
bst.insert(7)
bst.insert(3)
bst.insert(9)
bst.insert(13)
print(bst)
bst.delete(11)
print(bst)
bst.delete(5)
print(bst)
print("\nInorder Traversal - ",end="")
bst.inorder(bst.root)
print("\nPostorder Traversal - ",end="")
bst.postorder(bst.root)
print("\nPreorder Traversal - ",end="")
bst.preorder(bst.root)


    # def __repr__(self):
    #     return repr(self.root)

    # def childNodes(i):
    #     return (2*i)+1, (2*i)+2