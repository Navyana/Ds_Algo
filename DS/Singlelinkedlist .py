class Node:
    def __init__(self, data):
        self.item = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_List(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.item)
                temp = temp.next

    def insert_at_start(self, data):
        temp = self.head
        if (temp == None):
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def insert_at_end(self, data):
        temp = self.head
        if (temp == None):
            self.head = Node(data)
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    def delete_at_start(self):
        temp = self.head
        if (temp == None):
            print("No elements in the list to delete")
        else:
            temp = self.head
            self.head= self.head.next
            del temp

    def delete_at_end(self):
        temp = self.head
        if (temp == None):
            print("No elements in the list to delete")
        while temp.next.next is not None:
            temp = temp.next
        t = temp.next
        temp.next = None
        del t


list = LinkedList()
list.insert_at_end(1)
list.insert_at_start(2)
list.insert_at_end(3)
list.delete_at_start()
list.delete_at_end()
list.traverse_List()
