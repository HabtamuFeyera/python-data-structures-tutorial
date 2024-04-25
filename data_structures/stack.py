class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# Example usage
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
