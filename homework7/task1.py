import copy

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        result = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                 result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result)


my_matrix1 = Matrix([[31, 22, 3],
                    [37, 43, 2],
                    [51, 86, -1]])
my_matrix2 = Matrix([[3, 1, 2],
                    [7, 7, 3],
                    [4, 5, 9]])
new_matrix = my_matrix1 + my_matrix2
print(new_matrix)
