from logging import currentframe


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

    def insert_at_position(self,data,position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 0
        while current and count < position-1:
            current = current.next
            count +=1
        if current in None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node


    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
        else:
            print("The list is empty")

    def delete_at_end(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
            return

        last = self.head
        while last.next and last.next.next:
            last = last.next
        last.next = None


li = SinglylinkedList()
li.insert_at_beginning(5)
li.insert_at_beginning(6)
li.insert_at_beginning(1)
li.insert_at_last(1)
li.display()