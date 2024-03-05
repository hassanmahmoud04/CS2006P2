# Import necessary modules
import math  # For mathematical operations, if needed
import timeit  # For measuring execution time of small code snippets
from intricate_integer import IntricateInteger  # Import IntricateInteger class
from intricate_integers import IntricateIntegers  # Import IntricateIntegers class
from easy_medium_features import *  # Import all from easy_medium_features module

# Function to check if every element in the set has the intricate peculiar property
def iterator_has_intricate_peculiar_property(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)  # Create a set of IntricateIntegers
    for elem in intricate_integers:  # Iterate through each element
        # Check if squaring the element changes its value
        if (elem * elem).value != elem.value:
            return False  # If any element fails the property, return False
    return True  # If all elements pass, return True

# Function to check if associative property holds for all combinations of three elements in the set
def iterator_has_associative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)  # Create a set of IntricateIntegers
    for x, elem in enumerate(intricate_integers, 0):  # Enumerate elements starting from index 0
        for y, elem2 in enumerate(intricate_integers, 1):  # Nested enumeration starting from index 1
            for z, elem3 in enumerate(intricate_integers, 2):  # Another nested enumeration starting from index 2
                # Check if associative property holds: (a*b)*c == a*(b*c)
                if not (((elem * elem2) * elem3).value == (elem * (elem2 * elem3)).value):
                    return False  # If any combination fails, return False
    return True  # If all combinations pass, return True

# Function to check if commutative property holds for all pairs of elements in the set
def iterator_has_commutative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)  # Create a set of IntricateIntegers
    for i, elem in enumerate(intricate_integers, 0):  # Enumerate elements starting from index 0
        for j, elem2 in enumerate(intricate_integers, 1):  # Nested enumeration starting from index 1
            # Check if commutative property holds: a*b == b*a
            if not ((elem * elem2).value == (elem2 * elem).value):
                return False  # If any pair fails, return False
    return True  # If all pairs pass, return True

# Test and print results for associativity for values of n from 1 to 20 and corresponding alphas
associativity_results = []  # Initialize an empty list to store results where associativity holds
for n in range(1, 21):  # Loop through values of n
    for alpha in range(n):  # Loop through possible alpha values for each n
        # Check if associativity holds and append the pair (n, alpha) to the results list if it does
        if iterator_has_associative_intricate_multiplication(n, alpha):
            associativity_results.append((n, alpha))

print("Pairs (n, alpha) where associativity holds:", associativity_results)  # Print the results

# Demonstrate iteration over a set of IntricateIntegers and print each element
intricate_set = IntricateIntegers(3, 2)  # Create an IntricateIntegers set
print("IntricateIntegers(3, 2):")  # Header for printing
for x in intricate_set:  # Iterate through the set
    print(x)  # Print each IntricateInteger

# Function to compare execution times of associative and commutative property checks using iterators vs loops
def compare_times(n, alpha):
    # Time the execution of associative property check using iterator
    iterator_assoc = timeit.timeit(lambda: iterator_has_associative_intricate_multiplication(n, alpha), number=10000)
    # Time the execution of associative property check using a direct loop (assumed to be another function)
    loop_assoc = timeit.timeit(lambda: has_associative_intricate_multiplication(n, alpha), number=10000)
    # Print the results for associative property checks
    print("Time for 10000 tests for iterator associativity: " + str(iterator_assoc))
    print("Time for 10000 tests for loop associativity: " + str(loop_assoc))
    print("Difference: " + str(abs(loop_assoc - iterator_assoc)))

    # Repeat the process for commutative property checks
    iterator_commut = timeit.timeit(lambda: iterator_has_commutative_intricate_multiplication(n, alpha), number=10000)
    loop_commut = timeit.timeit(lambda: has_commutative_intricate_multiplication(n, alpha), number=10000)
    print("Time for 10000 tests for iterator commutativity: " + str(iterator_commut))
    print("Time for 10000 tests for loop commutativity: " + str(loop_commut))
    print("Difference: " + str(abs(loop_commut - iterator_commut)))

# Demonstrate the time comparison function for a specific pair of n and alpha
print("Comparing times for (3,2):")
compare_times(3, 2)
