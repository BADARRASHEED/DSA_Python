class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        # Case-1: If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Case-2: If the list is not empty
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_start(self, data):
        new_node = Node(data)

        # Case-1: If the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Case-2: If the list is not empty
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_before(self, target, data):
        current = self.head

        while current and current.data != target:
            current = current.next

        if current is None:
            return False

        new_node = Node(data)

        # inserting before head
        if current == self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return True

        # inserting in middle
        new_node.prev = current.prev
        new_node.next = current
        current.prev.next = new_node
        current.prev = new_node
        return True

    def insert_after(self, target, data):
        current = self.head

        # Find the target node
        while current and current.data != target:
            current = current.next

        # Target not found
        if current is None:
            return False

        new_node = Node(data)

        # Case: Inserting after the tail
        if current == self.tail:
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
            return True

        # Case: Inserting in the middle
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        return True

    def delete(self, key):
        current = self.head

        while current and current.data != key:
            current = current.next

        # Not found
        if current is None:
            return False

        # If node to be deleted is head
        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return True

        # If node to be deleted is tail
        if current == self.tail:
            self.tail = current.prev
            self.tail.next = None
            return True

        # Node is in the middle
        current.prev.next = current.next
        current.next.prev = current.prev
        return True

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    dll.insert_at_start(5)

    dll.insert_before(10, 7)

    dll.insert_after(20, 25)

    dll.display_forward()

    dll.display_backward()
