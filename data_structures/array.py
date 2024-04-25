class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __len__(self):
        return self.size

# Example usage
arr = Array(5)
arr[0] = 1
arr[1] = 2
arr[2] = 3
print(arr[1])  # Output: 2
print(len(arr))  # Output: 5
