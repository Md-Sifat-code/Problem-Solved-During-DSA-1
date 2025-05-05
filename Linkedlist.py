class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedlist:
    def __init__(self):
        self.head = None

    def inset_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        if not current:
            return  "The list is empty"
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

li = SinglyLinkedlist()
li.inset_at_end(2)
li.inset_at_end(4)
li.inset_at_end(6)
li.inset_at_end(1)
li.inset_at_end(8)
li.display()



