class CircularQueue:
    """
    CircularQueue implements a fixed-size circular (ring) buffer using an array.

    Key properties:
    - FIFO (First-In, First-Out) data structure
    - Uses modulo arithmetic to reuse freed slots
    - Avoids shifting elements (O(1) enqueue and dequeue)

    Invariants:
    - head points to the front (oldest) element
    - tail points to the next insertion position
    - size tracks the current number of elements
    """

    def __init__(self, capacity: int):
        """
        Initialize an empty circular queue with a fixed capacity.

        Args:
            capacity (int): Maximum number of elements the queue can hold

        Raises:
            ValueError: If capacity is not a positive integer
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        """
        Check whether the queue is empty.

        Returns:
            bool: True if the queue has no elements, False otherwise
        """
        return self.size == 0

    def is_full(self) -> bool:
        """
        Check whether the queue is full.

        Returns:
            bool: True if the queue has reached its capacity, False otherwise
        """
        return self.size == self.capacity

    def enqueue(self, item) -> None:
        """
        Insert an element at the rear of the queue.

        Time Complexity:
            O(1)

        Args:
            item: The element to be inserted

        Raises:
            OverflowError: If the queue is already full
        """
        if self.is_full():
            raise OverflowError("Queue is full")

        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        """
        Remove and return the front element of the queue.

        Time Complexity:
            O(1)

        Returns:
            The element removed from the front of the queue

        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.queue[self.head]
        self.queue[self.head] = None  # Clear slot (optional, for clarity)
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        """
        Return the front element without removing it.

        Returns:
            The front element of the queue

        Raises:
            IndexError: If the queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")

        return self.queue[self.head]

    def __len__(self) -> int:
        """
        Return the current number of elements in the queue.

        Returns:
            int: Number of elements
        """
        return self.size

    def __str__(self) -> str:
        """
        Return a human-readable string representation of the queue
        from front to rear.

        Returns:
            str: String representation of the queue
        """
        items = []
        idx = self.head
        for _ in range(self.size):
            items.append(str(self.queue[idx]))
            idx = (idx + 1) % self.capacity

        return f"CircularQueue([{', '.join(items)}])"


# Example usage:
if __name__ == "__main__":
    cq = CircularQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print(cq)  # CircularQueue([1, 2, 3])
    print(cq.dequeue())  # 1
    print(cq.peek())  # 2
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    print(cq)  # CircularQueue([2, 3, 4, 5, 6])
    print(cq.is_full())  # True
