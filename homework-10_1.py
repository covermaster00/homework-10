class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        _ = ''
        for row in self.matrix:
           _ += ' '.join(list(map(str, row))) + '\n'
        return f'{_}'

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])

    def __getitem__(self, item):
        return self.matrix[item]


matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[1, 1], [1, 1]])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
