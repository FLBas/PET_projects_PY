from classMatrix import Matrix
import unittest

class TestMatrix(unittest.TestCase):
    def test_sum_matrix(self):
        matrix1 = Matrix(2, 2)
        matrix1.set_matrix([[1, 2], [3, 4]])

        matrix2 = Matrix(2, 2)
        matrix2.set_matrix([[5, 6], [7, 8]])

        result = matrix1.SumMatrix(matrix2)
        
        expected = Matrix(2, 2)
        expected.set_matrix([[6, 8], [10, 12]])
        
        self.assertEqual(result, expected)

    def test_sub_matrix(self):
        matrix1 = Matrix(2, 2)
        matrix1.set_matrix([[5, 6], [7, 8]])

        matrix2 = Matrix(2, 2)
        matrix2.set_matrix([[1, 2], [3, 4]])

        result = matrix1.SubMatrix(matrix2)
        
        expected = Matrix(2, 2)
        expected.set_matrix([[4, 4], [4, 4]])

        self.assertEqual(result, expected)
    

    def test_mul_number(self):
        matrix = Matrix(2, 2)
        matrix.set_matrix([[1, 2], [3, 4]])

        result = matrix.MulNumber(3)
        
        expected = Matrix(2, 2)
        expected.set_matrix([[3, 6], [9, 12]])

        self.assertEqual(result, expected)

    def test_transpose(self):
        matrix = Matrix(2, 3)
        matrix.set_matrix([[1, 2, 3], [4, 5, 6]])

        result = matrix.Transpose()

        # Ожидаемый результат для транспонирования матрицы
        expected = Matrix(3, 2)
        expected.set_matrix([[1, 4], [2, 5], [3, 6]])

        self.assertEqual(result, expected)

    def test_determinant_2x2(self):
        matrix = Matrix(2, 2)
        matrix.set_matrix([[3, 4], [2, 1]])
        result = matrix.Determinant()


        self.assertEqual(result, -5)

    def test_determinant_3x3(self):
        matrix = Matrix(3, 3)
        matrix.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

        result = matrix.Determinant()


        self.assertEqual(result, 0)

    def test_invalid_determinant(self):
        matrix = Matrix(2, 3)
        with self.assertRaises(ValueError):
            matrix.Determinant()

    def test_calc_complements(self):
        matrix = Matrix(3, 3)
        matrix.set_matrix([[4, 3, 2], [1, 5, 6], [7, 8, 9]])

        result = matrix.CalcComplements()

        expected = Matrix(3, 3)
        expected.set_matrix([[-3, 33, -27], [-11, 22, -11], [8, -22, 17]])

        self.assertEqual(result, expected)

    def test_get_minor(self):
        matrix = Matrix(3, 3)
        matrix.set_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        temp = Matrix(2, 2)
        matrix.get_minor(0, 0, temp)
        
        expected_minor = Matrix(2, 2)
        expected_minor.set_matrix([[5, 6], [8, 9]])

        self.assertEqual(temp, expected_minor)

if __name__ == "__main__":
    unittest.main()