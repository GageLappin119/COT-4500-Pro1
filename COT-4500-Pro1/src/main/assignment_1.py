import math
from sympy import *
from sympy import symbols, lambdify

def approximation_alg(value_to_approximate, exponent, tol):
    x0 = value_to_approximate / (math.pow(value_to_approximate, 1 / exponent))

    if x0 == int(x0):  # If x0 is already an integer, no iterations are needed
        return 0

    x0 = value_to_approximate / (exponent + 1) * 2

    iterations = 0
    diff = x0
    x = x0

    while diff >= tol:
        print(iterations, ": ", x)
        iterations += 1
        prev_x = x
        x = (x / 2) + (1 / x)
        diff = abs(x - prev_x)

    return iterations

def bisection_method(error, a, b, f):
    x = symbols('x')  # Symbol for symbolic expressions
    f_numeric = lambdify(x, f)  # Convert symbolic function to a numerical function

    # Check if the interval is valid
    if f_numeric(a) * f_numeric(b) >= 0:
        raise ValueError("The function must have opposite signs at a and b.")

    iterations = 0
    precision = abs(b - a)

    while precision > error:
        iterations += 1
        midpoint = (a + b) / 2
        mid_val = f_numeric(midpoint)
        print(iterations, ": ", mid_val)


        # Update interval
        if f_numeric(a) * mid_val < 0:
            b = midpoint
        else:
            a = midpoint

        # Update precision
        precision = abs(b - a)

        # Stop explicitly if maximum iterations is reached
        if iterations >= 100:
            break

    # Return the midpoint and number of iterations
    return midpoint, iterations

def fixed_point_iteration(error, f, f_0):
    x = symbols('x')
    tol = error  # Use the provided error as the tolerance
    max_iterations = 50

    a, b = 0, 0
    iter = 0
    if f_0.subs(x, iter) > 0:
        while (f_0.subs(x, iter) > 0) and iter > -100:
            iter = iter - 1
        b = iter 
        a = iter - 1
    else:
        while (f_0.subs(x, iter) < 0) and iter < 100:
            iter = iter + 1
        b = iter
        a = iter - 1

    if iter >= 100 or iter <= -100:
        return 0
    x0 = (a + b) / 2

    iterations = 0
    while iterations < max_iterations:
        print(iterations, ": ", x0)
        next_x = f.subs(x, x0)

        # Check for divergence
        if math.isinf(next_x):
            return 0  # Indicate failure due to divergence

        # Check for convergence
        if abs(next_x - x0) < tol:
            return iterations + 1

        iterations += 1
        x0 = next_x

    return 0  # Return 0 to indicate failure if max iterations reached



def newton_raphson_method(f, f_prime, initial_guess, tolerance=1e-4, max_iterations=100):
    x = symbols('x')
    guess = initial_guess

    for iterations in range(1, max_iterations + 1):
        print(iterations, ": ", guess)
        f_value = f.subs(x, guess)
        f_prime_value = f_prime.subs(x, guess)

        # Avoid division by zero
        if abs(f_prime_value) < tolerance:
            return 0  # Indicate failure due to zero derivative

        next_guess = guess - f_value / f_prime_value

        # Check for convergence
        if abs(next_guess - guess) <= tolerance:
            return iterations

        guess = next_guess

    return 0  # Return 0 to indicate failure if max iterations reached



