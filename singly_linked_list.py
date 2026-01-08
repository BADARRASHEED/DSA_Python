class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end of the list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Insert a new node at the start of the list
    def insertAtStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node in the middle of the list
    def insertInMiddle(self, data):
        if not self.head:
            self.head = Node(data)
            return

        slow = self.head
        fast = self.head

        # fast moves 2x, slow moves 1x
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now the left-middle node
        new_node = Node(data)
        new_node.next = slow.next
        slow.next = new_node

    # Delete a node by key
    def deleteNode(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    # Print the linked list
    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insertAtEnd(10)
    sll.insertAtEnd(20)
    sll.insertAtStart(5)
    sll.insertInMiddle(15)
    sll.printLL()  # Output: 5 -> 10 -> 15 -> 20 -> None
    sll.deleteNode(20)
    sll.printLL()  # Output: 5 -> 10 -> 15 -> None
