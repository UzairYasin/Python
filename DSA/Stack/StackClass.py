class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return "Stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):
        if self.head is None:
            return "Stack is Empty"
        return self.head.data


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

while stack.head is not None:
    print(stack.peek())
    stack.pop()