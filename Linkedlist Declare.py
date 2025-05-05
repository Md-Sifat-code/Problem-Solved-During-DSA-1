class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglylinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        if not  current:
            return "List is empty"

        while current:
            print(current.data, end="->")
            current = current.next

        print("None")
    def insert_at_last(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node



li = SinglylinkedList()
li.insert_at_beginning(5)
li.insert_at_beginning(6)
li.insert_at_beginning(1)
li.insert_at_last(1)
li.display()