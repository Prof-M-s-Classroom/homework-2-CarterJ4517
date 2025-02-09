from Spaceship import Spaceship


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        return str(self.head)

    def append(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0):
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def dellast(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# TODO : Write function insertatindex to insert a newnode at any given index. Consider all edge cases, including missing nodes.
# TODO : Write fucntion deleteatindex to delete a newnode at any given index. COnsider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

    # insertatindex: creates a new node with given value and inserts it at given index
    def insertatindex(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:    # edge case: given index out of bounds
            return False
        elif self.length == 0:                  # edge case: list begins with no nodes
            self.head = new_node
            self.tail = new_node
        elif index == 0:                        # edge case: given index is at list beginning (prepends)
            return self.prepend(value)
        elif index == self.length:              # edge case: given index is at list end (appends)
            return self.append(value)
        else:                                   # iterates to given index and inserts new data
            pre = self.head
            temp = self.head
            for i in range(index):
                pre = temp
                temp = temp.next
            pre.next = new_node
            new_node.next = temp
        self.length += 1
        return True

    # deleteatindex: removes the node at a given index
    def deleteatindex(self, index):
        if index < 0 or index >= self.length:   # edge case: given index is out of bounds
            return self.head
        elif self.length == 0:                  # edge case: list is empty
            return None
        elif index == 0:                        # edge case: index is at beginning of list (deletes first node)
            return self.delfirst()
        elif index == self.length-1:            # edge case: index is at end of list (deletes last node)
            return self.dellast()
        else:                                   # iterates to given index and removes corresponding node
            pre = self.head
            temp = self.head
            for i in range(index):
                pre = temp
                temp = temp.next
            pre.next = temp.next
            self.length -= 1
            return temp

# Test code:

s0 = Spaceship("TEST", 300)
s1 = Spaceship("Voyager", 300)
s2 = Spaceship("Enterprise", 300)
s3 = Spaceship("Atlantis", 300)
s4 = Spaceship("Challenger", 300)
s5 = Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
print()
deleted = mylinkedlist.insertatindex(1,s0)
mylinkedlist.print_list()
print()

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
print()
deleted = mylinkedlist.deleteatindex(0)
print(deleted)
print()
mylinkedlist.print_list()