import matrix

matrix_1 = matrix.Matrix(4,5,6,7)
matrix_2 = matrix.Matrix(2,2,2,1)


matrix_1.print_matrix()
matrix_2.print_matrix()


matrix_3 = matrix_2 + 1
matrix_3.print_matrix()

matrix_4 = matrix_1 * matrix_2
matrix_4.print_matrix()

matrix_5 = matrix_1 + matrix_2
