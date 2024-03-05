# Import necessary modules and functions
import timeit  # Module for timing code execution
import pytest  # Module for advanced testing functionalities
from easy_medium_features import *  # Imports all from easy_medium_features module
from i_integerwith_medium_features import *  # Imports all from i_integerwith_medium_features module
from intricate_integer_hardfeatures import *  # Imports all from intricate_integer_hardfeatures module
from intricate_integer import IntricateInteger  # Specific import of the IntricateInteger class
from intricate_integers import IntricateIntegers  # Specific import of the IntricateIntegers class
from itertools import combinations  # Import combinations function for generating combinations of elements

# Test function for validating the handling of incompatible IntricateInteger instances
def test_intricate_integer_mismatch():
    print("Testing IntricateIntegerMismatch exception...")
    try:
        # Creating two IntricateInteger instances with different alpha values to trigger an exception
        int1 = IntricateInteger(1, 100, 10)  # Example instance with alpha=10
        int2 = IntricateInteger(2, 100, 20)  # Another instance with a different alpha=20
        result = int1 * int2  # Attempting multiplication should raise an exception due to mismatch
        assert False, "IntricateIntegerMismatch was not raised as expected."  # This line should not be executed
    except IntricateIntegerMismatch:
        print("IntricateIntegerMismatch raised successfully for incompatible IntricateIntegers.")  # Expected outcome

# Test function for basic operations of IntricateInteger instances
def test_intricate_integer():
    # Creating two IntricateInteger instances for testing
    x = IntricateInteger(3, 7, 2)  # Instance with value=3, modulus=7, alpha=2
    y = IntricateInteger(5, 7, 2)  # Another instance with value=5
    # Performing assertions to validate string representation and mathematical operations
    assert str(x) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x)}'"
    assert str(y) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(y)}'"
    assert str(x * x) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(x * x)}'"
    assert str(x * y) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x * y)}'"
    try:
        # Creating a new IntricateInteger instance with a different modulus to trigger an exception
        z = IntricateInteger(1, 8, 3)  # Different modulus
        result = x * z  # Attempting multiplication should raise an exception
        assert False, "Expected ValueError for incompatible IntricateIntegers"  # This line should not be executed
    except ValueError:
        pass  # Expected exception for incompatible operations
    print("IntricateInteger basic tests passed!")

# Function to generate and return results for peculiar and commutative properties
def peculiar_commutative_results():
    # Initializing lists to store results
    peculiar_property_results = []  # Stores results where peculiar property holds
    ipeculiar_property_results = []  # Stores results from an iterative check for peculiar property
    commutative_property_results = []  # Stores pairs where commutative property does not hold
    icommutative_property_results = []  # Stores pairs from an iterative check where commutativity does not hold
    # Looping through a range to check for properties and fill the lists accordingly
    for n in range(1, 51):
        # Generating results based on has_intricate_peculiar_property and has_commutative_intricate_multiplication functions
        peculiar_property_results += [(n, a) for a in range(0, n) if has_intricate_peculiar_property(n, a)]
        ipeculiar_property_results += [(n, a) for a in range(0, n) if iterator_has_intricate_peculiar_property(n, a)]
        commutative_property_results += [(n, a) for a in range(0, n) if not has_commutative_intricate_multiplication(n, a)]
        icommutative_property_results += [(n, a) for a in range(0, n) if not iterator_has_commutative_intricate_multiplication(n, a)]
    return peculiar_property_results, ipeculiar_property_results, commutative_property_results, icommutative_property_results

# Generating results for peculiar and commutative properties
peculiar_property_results, ipeculiar_property_results, commutative_property_results, icommutative_property_results = peculiar_commutative_results()

# Pytest parametrized test for checking the peculiar property
@pytest.mark.parametrize("results_tuple", peculiar_property_results)
def test_peculiar_property(results_tuple):
    n, a = results_tuple  # Unpacking n and alpha from the tuple
    assert a == n-1, f"{a} = {n-1}"  # Asserting that alpha equals n-1 for the peculiar property to hold

# Pytest parametrized test for checking the iterative peculiar property
@pytest.mark.parametrize("results_tuple", ipeculiar_property_results)
def test_iterative_peculiar_property(results_tuple):
    n, a = results_tuple  # Unpacking n and alpha from the tuple
    assert a == n-1, f"{a} = {n-1}"  # Asserting that alpha equals n-1 for the peculiar property to hold iteratively

# Pytest fixture for commutative property tests
@pytest.fixture
def commutative_results(request):  
    return request.param  # Returning the parameterized input

# Pytest parametrized test for checking the commutative property
@pytest.mark.parametrize("commutative_results", commutative_property_results, indirect=True)
def test_commutative_property(commutative_results):
    assert len(commutative_results) == 0  # Asserting that there are no results where the commutative property does not hold

# Main test block for testing new features, including associative property and roots of one
print("Testing associative property and intricate roots of one...")
for n in range(1, 6):  # Looping through a sample range for n
    for alpha in range(0, n):  # Looping through possible alpha values
        # Printing out results of checks for associative property and roots of one
        print(f"n={n}, alpha={alpha}, associative: {has_associative_intricate_multiplication(n, alpha)}")
        print(f"n={n}, alpha={alpha}, roots of one: {intricate_roots_of_one(n, alpha)}")

# Generating and printing a spanning set from a set of IntricateInteger instances
w = IntricateInteger(3, 7, 2)
x = IntricateInteger(5, 7, 2)
y = IntricateInteger(6, 7, 2)
z = IntricateInteger(4, 7, 2)
span = generate_spanning_set([w, x, y, z])  # Generating the spanning set
for i in span:
    print(i)  # Printing each element in the spanning set
