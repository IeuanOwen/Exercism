class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in row.split()] for row in matrix_string.split("\n")]


    def row(self, index):
    	if index < 1:
    		print("Index out of Range")
    	return self.matrix[index-1]


    def column(self, index):
    	if index < 1:
    		print("Index out of Range")
    	else:
    		return [i[index-1]for i in self.matrix]