import math

class Matrix():
    def __init__(self, *values):
        self.values = values
        self.size = int(math.sqrt(len(values)))

    def print_matrix(self):
        nr_of_column = 0
        for value in self.values:
            print(value, end = " ")
            nr_of_column+=1
            if (nr_of_column%self.size == 0):
                print()
        print()

    def __add__(self, B):
        result_values = []

        if type(B) is int:
            for value in list(self.values):
                result_values.append(value + B)

        else:
            if (self.size == B.size):

                for value in list(self.values):
                    result_values.append(value + B.values[self.values.index(value)])

        result = Matrix(*result_values)
        return result

    def __mul__(self, B):
        result_values = []

        if (self.size == B.size):
            for i in range(self.size):
                for j in range(self.size):
                        sum = 0
                        for element in range(self.size):
                            sum += self.values[i*self.size+element]*B.values[j+element*self.size]
                        result_values.append(sum)

        result = Matrix(*result_values)
        return result


if __name__ == '__main__':
    main()
