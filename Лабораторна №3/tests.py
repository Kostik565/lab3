import unittest
import numpy as np
from main import generate_matrix, work_which_matrix

class TestMatrixFunctions(unittest.TestCase):
    
    def test_generate_matrix_shape(self):
        """Перевіряє, чи матриця має правильний розмір (3x4)."""
        a = generate_matrix()
        self.assertEqual(a.shape, (3, 4))
    
    def test_generate_matrix_range(self):
        """Перевіряє, чи всі елементи матриці знаходяться в межах [-10, 10)."""
        a = generate_matrix()
        self.assertTrue(np.all((a >= -10) & (a < 10)))
    
    def test_work_which_matrix(self):
        """Перевіряє коректність роботи функції work_which_matrix."""
        test_arr = np.array([[ 1, -6,  3,  7],
                             [-4, -8, -3, -4],
                             [ 3, -2, -7,  2]])
        
        M, even_columns, new_a, numbers = work_which_matrix(test_arr)

        expected_M = np.array([1, 4, 2])  # Кількість від'ємних чисел в кожному рядку
        expected_even_columns = np.array([[1, 3], 
                                          [-4, -3], 
                                          [3, -7]])  # Парні стовпчики
        expected_new_a = np.array([[-4, -8, -3, -4], 
                                   [3, -2, -7,  2]])  # Видалений перший рядок
        expected_numbers = np.array([1, 3, 7, 3, 2])  # Додатні числа
        
        np.testing.assert_array_equal(M, expected_M)
        np.testing.assert_array_equal(even_columns, expected_even_columns)
        np.testing.assert_array_equal(new_a, expected_new_a)
        np.testing.assert_array_equal(numbers, expected_numbers)

if __name__ == '__main__':
    unittest.main()