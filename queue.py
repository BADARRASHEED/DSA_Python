class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def length(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Front item:", q.peek())  # Output: Front item: 1

    print("Queue length:", q.length())  # Output: Queue length: 3
    print("Dequeue item:", q.dequeue())  # Output: Dequeue item: 1
    print(
        "Queue length after dequeue:", q.length()
    )  # Output: Queue length after dequeue: 2
