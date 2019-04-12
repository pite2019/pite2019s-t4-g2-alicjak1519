class Matrix():
    def __init__(self, *values):
        self.values = values

    def add(self, another_matrix):
        result = []

        for nr_of_value in range(0,4):
            result.append(self.values[nr_of_value] + another_matrix.values[nr_of_value])

        return result

    def product(self, another_matrix):

        result = []
        result.append(self.values[0]*another_matrix[0]+self.values[2]*another_matrix[3])
        result.append(self.values[0]*another_matrix[2]+self.values[2]*another_matrix[4])
        result.append(self.values[3]*another_matrix[0]+self.values[4]*another_matrix[3])
        result.append(self.values[3]*another_matrix[2]+self.values[4]*another_matrix[4])

        return result
