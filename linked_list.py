class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_node(self, value):
        if self.head is None:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        while current:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        print("Element not found in the linked list.")               

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()




print("Enter your choice:")
x=1
link= LinkedList()
while(x<4 and x>0):
    x=int(input("Enter 1 to add, 2 to remove, 3 to display and 4 to exit: "))
    if x==1:
        a=input("Enter your value: ")
        link.add_node(a)
    elif x==2:
        link.remove_node(input("Enter your value: "))
    elif x==3:
        link.display()

