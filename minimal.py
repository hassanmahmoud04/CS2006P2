import math
from itertools import product

# Assuming the IntricateInteger class and intricate_roots_of_one function are implemented as provided.
# Adjust these import statements according to your project structure.
from intricate_integer import IntricateInteger
from intricate_integer_hardfeatures import intricate_roots_of_one  # Replace 'your_module' with the actual module name.

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def find_counterexample():
    # Starting the search from n=2 to avoid the trivial case where n=1
    for n in range(2, 51):
        for alpha in range(1, n, 2):  # Iterate over odd values of alpha
            if gcd(n, alpha) != 1:
                roots = intricate_roots_of_one(n, alpha)
                if roots:
                    return n, alpha, roots
    return None, None, None

n, alpha, roots = find_counterexample()
if n is not None:
    print(f"Counterexample found: n = {n}, alpha = {alpha}, roots = {roots}")
else:
    print("No counterexample found within the search range.")
