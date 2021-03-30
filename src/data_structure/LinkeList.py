class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        """Initialize head and tail attribute of linked list for sentinels control"""
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        """Get length of linked list"""
        return self.size

    def is_empty(self):
        """Function that check if linked list id empty"""
        return self.size == 0

    def get_last(self):
        """Function that return the last item of linked list with modifying it"""
        return self.tail.data

    def get_first(self):
        """Function that return the first item of linked list with modifying it"""
        return self.head.data

    def add_head(self, data):
        """Function that insert data at the beginning of linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def add_tail(self, data):
        """Function that insert data at the end of linked list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head

        self.tail.next = new_node
        new_node.prev = self.head
        self.tail = new_node

        self.size += 1

    def remove_head(self):
        """Function that remove data at the beginning of linked list"""
        removedNode = self.head

        if not self.head:
            return None
        self.head = self.head.next
        self.head.prev = None

        self.size -= 1
        return removedNode.data

    def remove_tail(self):
        """Function that remove data at the end of linked list"""
        removedNode = self.tail

        if not self.head:
            return None

        self.tail = removedNode.prev
        self.tail.next = None

        self.size -= 1
        return removedNode.data

    def find(self, index):
        """Function that find a specific node at index specify in a linked list"""
        if index < 0 or index >= self.size:
            return None

        if index <= self.size // 2:
            currentNode = self.head
            count = 0
            while count < index:
                currentNode = currentNode.next
                count += 1
        else:
            currentNode = self.head
            count = index
            while count <= index:
                currentNode = currentNode.prev
                count -= 1
        return currentNode

    def insert(self, data, index):
        """Method that insert data at any position in a linked list"""
        if index < 0 or index > self.size:
            return None

        if index == self.size:
            self.add_tail(data)
        if index == 0:
            self.add_head(data)

        nextNode = self.find(index - 1)
        newNode = Node(data)

        temp = nextNode.next

        nextNode.next = newNode
        newNode.next = temp
        newNode.prev = nextNode

        self.size += 1

    def remove(self, index):
        if index < 0 or index > self.size:
            return None
        if index == self.size:
            self.remove_tail()
        if index == 0:
            self.remove_head()

        removeNode = self.find(index)

        removeNode.prev.next = removeNode.next
        removeNode.next.prev = removeNode.prev

        self.size -= 1
        return removeNode.data

    def update(self, data, index):
        updatedNode = self.find(index)
        if updatedNode:
            updatedNode.data = data
        return updatedNode.data


linked_list = LinkedList()

linked_list.add_tail(54)
linked_list.add_tail("Hello")
linked_list.add_tail([632, 737, 73])

linked_list.add_head(54)
linked_list.add_head("Hello")
linked_list.add_head([632, 737, 73])
linked_list.add_head({"greet": "Hello dear"})

print(f"Size of item in linked list: {linked_list.get_size()}")
print(f"First Item of the linked list: {linked_list.get_first()}")
print(f"Last Item of the linked list: {linked_list.get_last()}")

print(f"Remove item from head of liked list: {linked_list.remove_head()}")
print(f"Size of item in linked list: {linked_list.get_size()}")

print(f"Remove item from tail of liked list: {linked_list.remove_tail()}")
print(f"Size of item in linked list: {linked_list.get_size()}")

print(f"Data of element at index 2 on linked list {linked_list.find(1)}")

print(f"Size of item in linked list before insert: {linked_list.get_size()}")
print("============================")
linked_list.insert(3, 1)
print(f"Size of item in linked list after insert: {linked_list.get_size()}")

print("************************************************************")

print(f"Size of item in linked list before remove: {linked_list.get_size()}")
print("============================")
linked_list.remove(3)
print(f"Size of item in linked list after remove: {linked_list.get_size()}")

print("************************************************************")

linked_list.update(89, 3)

