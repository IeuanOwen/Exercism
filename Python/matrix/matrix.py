class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split("\n")]


    def row(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        try:
    	    return self.matrix[index-1]
        except:
            raise IndexError("Index out of range")


    def column(self, index):
        if index < 0:
            raise IndexError("Index out of range")
        try:
            print([i[index-1]for i in self.matrix])
            return [i[index-1]for i in self.matrix]
        except:
            print(2)
            raise IndexError("Index out of range")
