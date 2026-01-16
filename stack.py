class Stack:
    def __init__(self):
        self.items = []

    def length(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Top item is:", stack.peek())  # Output: Top item is: 3
    print("Stack length is:", stack.length())  # Output: Stack length is: 3
    print("Popped item is:", stack.pop())  # Output: Popped item is: 3
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
