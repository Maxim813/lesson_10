class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix_ = [[0, 1, 2],
                [0, 1, 2],
                [3, 4, 5]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matrix_[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix_]))



my_matrix = Matrix([[5, 6, 9],
                    [3, 2, 4],
                    [4, 4, 5]],
                   [[4, 8, 2],
                    [6, 4, 3],
                    [2, 5, 7]])



print(my_matrix.__add__())