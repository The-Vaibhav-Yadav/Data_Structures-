class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top.next = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return False
        if self.height == 1:
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp.value

    def fibonacci(self):
        n=int(input("Enter No."))
        temp1 = self.top
        temp2 = self.top
        for _ in range(2, n):
            new_value = temp1.value + temp2.value
            self.push(new_value)
            temp2 = temp1
            temp1 = Node(new_value)
        return self.top.value


mystack = Stack(1)
print(mystack.fibonacci())
