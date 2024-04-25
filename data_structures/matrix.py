class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]
    
    def __getitem__(self, indices):
        row, col = indices
        return self.data[row][col]
    
    def __setitem__(self, indices, value):
        row, col = indices
        self.data[row][col] = value

# Example usage
matrix = Matrix(2, 3)
matrix[0, 0] = 1
matrix[0, 1] = 2
matrix[1, 2] = 3
print(matrix[0, 1])  # Output: 2
