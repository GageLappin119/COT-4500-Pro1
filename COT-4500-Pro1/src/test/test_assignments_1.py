import unittest
import sys
import os
from sympy import symbols, Eq, solve

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.assignment_1 import (  
    approximation_alg,
    bisection_method,
    fixed_point_iteration,
    newton_raphson_method
)

class TestAssignment1(unittest.TestCase):
    def test_approximation_alg(self):
        # Test approximation_alg for various cases
        value_to_approximate = 2
        exponent = 2
        tolerance = 10 ** -6
        result = approximation_alg(value_to_approximate, exponent, tolerance)
        self.assertIsInstance(result, int, "Result should be an integer representing the iterations.")
        self.assertGreaterEqual(result, 0, "Iterations should be non-negative.")
        print(f"\nIterations for approximation_alg: {result}")

    def test_bisection_method(self):
        # Test bisection_method with a simple case
        x = symbols('x')
        f = x**3+4*x**2-10
        a, b = -4, 7
        error = 10 ** -4

        result = bisection_method(error, a, b, f)
        self.assertIsInstance(result, tuple, "Result should be a tuple (root, iterations).")
        self.assertGreaterEqual(result[1], 0, "Iterations should be non-negative.")
        print(f"\nRoot: {result[0]}, Iterations for bisection_method: {result[1]}")

    def test_fixed_point_iteration(self):
        # Test fixed_point_iteration with a simple function

        x = symbols('x')

        f_0 = 2*x**3 - 2 * x - 5
        f = ((2*x+5) / 2)**(1/3)
        
        error = 0.00001

        result = fixed_point_iteration(error, f, f_0)
        self.assertGreaterEqual(result, 0, "Iterations should be non-negative.")
        print(f"\nIterations for fixed_point_iteration: {result}")

    def test_newton_raphson_method(self):
        # Test Newton-Raphson method with a simple function
        x = symbols('x')
        f = x**3 + 4*x**2 - 10
        f_prime = f.diff(x)
        
        initial_guess = 1
        tolerance = 10 ** -4

        result = newton_raphson_method(f, f_prime, initial_guess, tolerance)
        self.assertGreaterEqual(result, 0, "Iterations should be non-negative.")
        print(f"\nIterations for newton_raphson_method: {result}")


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=0).run(unittest.TestLoader().loadTestsFromTestCase(TestAssignment1))

