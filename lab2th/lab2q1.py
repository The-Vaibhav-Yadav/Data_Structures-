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
        return temp
    
    def sum_till_n(self):
        num=int(input("Enter number"))
        while num!=0:
            self.push(num)
            num=num-1

        result=0
        temp=self.top
        while temp is not None:
            result=result+temp.value
            temp=temp.next
        print(result)


        
    
mystack=Stack(0)
mystack.sum_till_n()


