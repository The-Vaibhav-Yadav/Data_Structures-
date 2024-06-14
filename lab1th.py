int1=str(input("Number 1: "))
int2=str(input("Number 2: "))

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.lenght=1

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.lenght += 1

    def print_list(self):
        temp=self.head
        while temp is not None:
            print (temp.value)
            temp=temp.next

    def pop_first(self):    
        self.head=self.head.next

    def get(self,index):
        temp=self.head
        if index<0 or index>=self.lenght:
            return None
        else:
            for _ in range(index):
                temp=temp.next
            return temp
        
    def set_value(self,index,value):
        temp=self.get(index)
        if temp:        
            temp.value=value
            return True
        return False
    

        
ExtendedInt1 = LinkedList(0)
ExtendedInt2 = LinkedList(0)
ExtendedInt1.pop_first()
ExtendedInt2.pop_first()


for i in range(len(int1)):   
    ExtendedInt1.append((int1[i:i+1]) or 0)

for i in range(len(int1)):   
    ExtendedInt2.append((int2[i:i+1]) or 0)




ExtendedInt1.addition


# ExtendedInt1.print_list()
# ExtendedInt2.print_list()


