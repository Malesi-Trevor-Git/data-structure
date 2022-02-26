

class Stack:
    def __init__(self):
        self.stack = []
    #add items to Stack
    def push(self,item):
        self.stack.append(item)
    #remove items from Stack
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[len(self.stack)-1]
#create an instance of the stack object
s=Stack()
s.push(1)
s.push(2)
s.push(3)
class Queue:
    def __init__(self):
        self.queue = []
    #add items
    def enqueue(self,item):
        self.queue.append(item)
    #remove items
    def dequeue(self):
        return self.queue.pop(0)
    #return elements of the queue
    def queue_items(self):
        return self.queue
#create an instance of the queue object
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.queue_items())
q.dequeue()
class Tree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
    #insert items to the Tree
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Tree(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data

    #print the tree structure
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    #tree traversal algorithms
    #root->left->right
    def preorder_traversal(self,root):
        preorder=[]
        if root:
            preorder.append(root.data)
            preorder=preorder+self.preorder_traversal(root.left)
            preorder=preorder+self.preorder_traversal(root.right)
        return preorder
    #inorder traversal
    #left->root->right
    def inorder_traversal(self,root):
        inorder=[]
        if root:
            inorder=self.inorder_traversal(root.left)
            inorder.append(root.data)
            inorder=inorder+self.inorder_traversal(root.right)
        return inorder
    #postorder traversal
    #left->right->root
    def postorder_traversal(self,root):
        postorder=[]
        if root:
            postorder=self.postorder_traversal(root.left)
            postorder=postorder+self.postorder_traversal(root.right)
            postorder.append(root.data)
        return postorder

#create an instance of the tree structure
t=Tree(27)
t.insert(14)
t.insert(35)
t.insert(10)
t.insert(19)
t.insert(31)
t.insert(42)

#linked list
#singly linked list
class SinglyLinkedListNode:
    def __init__(self,data=None):
        self.data = data
        self.next =None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def printSinglyLinkedList(self):
        value=self.head
        while value is not None:
            print(value.data)
            value=value.next
#create an instance of the singly linked list
s=SinglyLinkedList()
s.head=SinglyLinkedListNode("Monday")
second=SinglyLinkedListNode("Tuesday")
third=SinglyLinkedListNode("Wednesday")
s.head.next=second
second.next=third
s.printSinglyLinkedList()
