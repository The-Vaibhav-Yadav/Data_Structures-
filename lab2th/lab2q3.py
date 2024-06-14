class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1
    
    def print_list(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def push(self,value):
        new_node=Node(value)
        if self.height==0:
            self.top.next=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1

    def pop(self):       
        if self.height == 0:
            return False
        if self.height == 1:
            self.top=None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None
        self.height-=1
        return temp.value


    def is_palindrome(self):
        s=str(input("Enter palindrome "))
        s = s.lower()
        for char in s:
            self.push(char)        
        for char in s:
            if char != self.pop():
                return False      
        return True

mystack= Stack('')
print(mystack.is_palindrome())