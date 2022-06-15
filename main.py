#Linked List (All operations performed in Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node_front(self, newdata):
        newNode = Node(newdata)
        newNode.next = self.head
        self.head = newNode

    def add_after(self, prev, newdata):
        if prev is None:
            print("previous node should be given")
            return
        newNode = Node(newdata)
        newNode.next = prev.next
        prev.next = newNode

    def add_last(self, newdata):
        newNode = Node(newdata)

        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def add_random_nodes(self):
        self.head = Node(1)
        self.second = Node(2)
        self.third = Node(3)

        self.head.next = self.second
        self.second.next = self.third

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def delete(self, value):
        temp = self.head
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == value:
                break
        prev = temp
        temp = temp.next
        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def deleteNode(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return self.head
        index = 0
        current = self.head
        prev = self.head
        temp = self.head
        while current is not None:
            if index == position:
                temp = current.next
                break
            prev = current
            current = current.next
            index += 1
        prev.next = temp
        return prev
if __name__ == '__main__':
    llist = LinkedList()
    llist.add_random_nodes()
    llist.print_list()
    llist.delete(2)
    llist.print_list()
    llist.deleteNode(1)