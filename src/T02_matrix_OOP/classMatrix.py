
class Matrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._matrix = self.set_matrix()


    def get_rows(self):
        return self._rows
    
    def get_cols(self):
        return self._cols

    def set_matrix(self, value=None):
        if value is None:
            value = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

        self._matrix = value
        return self._matrix
    
    def get_matrix(self):
        for row in self._matrix:
            print(row)

    def __eq__(self, other):
        flag = False
        if isinstance(other, Matrix):
            flag = self._matrix == other._matrix

        return flag
    
    def SumMatrix(self, other):
        result = Matrix(self._rows, self._cols)

        if isinstance(other, Matrix) and self._rows == other._rows and self._cols == other._cols:
            for i in range(self._rows):
                for j in range(self._cols):
                    result._matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]
        else:
            raise ValueError("Матрицы должны быть одинакового размера для сложения")
            
        return result
    
    def SubMatrix(self, other):
        result = Matrix(self._rows, self._cols)

        if isinstance(other, Matrix) and self._rows == other._rows and self._cols == other._cols:
            for i in range(self._rows):
                for j in range(self._cols):
                    result._matrix[i][j] = self._matrix[i][j] - other._matrix[i][j]
        else:
            raise ValueError("Матрицы должны быть одинакового размера для сложения")
            
        return result
        
    def MulNumber(self, num):
        result = Matrix(self._rows, self._cols)
                        
        for i in range(self._rows):
                for j in range(self._cols):
                    result._matrix[i][j] = self._matrix[i][j] * num
        
        return result

    def Transpose(self):
        result = Matrix(self._cols, self._rows)
        
        for i in range(self._rows):
                for j in range(self._cols):
                    result._matrix[j][i] = self._matrix[i][j] 

        return result
    

    def CalcComplements(self):
        res = Matrix(self._rows, self._cols)
        
        if self._rows == 1:
            res._matrix[0][0] = self.Determinant()
        else:
            for i in range(self._rows):
                for j in range(self._cols):

                    temp = Matrix(self._rows - 1, self._cols - 1)
                    self.get_minor(i, j, temp)
                    
                    det = temp.Determinant()

                    sign = 1 if (i + j) % 2 == 0 else -1
                    res._matrix[i][j] = det * sign
        
        return res

    def Determinant(self):
        if self._rows != self._cols:
            raise ValueError("Матрица не является квадратной")
        
        res = 0
        
        if self._rows == 1:
            res = self._matrix[0][0]
        elif self._rows == 2:
            res = self._matrix[0][0] * self._matrix[1][1] - self._matrix[0][1] * self._matrix[1][0]
        else:
            for i in range(self._rows):
                temp = Matrix(self._rows - 1, self._cols - 1)
                self.get_minor(0, i, temp)
                
                det = temp.Determinant()

                sign = 1 if i % 2 == 0 else -1
                res += self._matrix[0][i] * det * sign
        
        return res

    def get_minor(self, row, col, temp):
        for i in range(self._rows):
            if i == row:
                continue
            for j in range(self._cols):
                if j == col:
                    continue
                temp._matrix[i if i < row else i - 1][j if j < col else j - 1] = self._matrix[i][j]

        return temp