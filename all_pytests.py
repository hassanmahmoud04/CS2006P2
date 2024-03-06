import timeit
import pytest  # Added for pytest functionalities
from easy_medium_features import *
from i_integerwith_medium_features import *
from intricate_integer_hardfeatures import *
from intricate_integers import IntricateIntegers

from itertools import combinations

@pytest.mark.parametrize("n, alpha, expected_roots", [
    (3, 2, {1}),  # Example expecting a specific root of one for these parameters
    # Add more (n, alpha, expected_roots_set) tuples
])
def test_intricate_roots_of_one(n, alpha, expected_roots):
    roots = intricate_roots_of_one(n, alpha)
    assert set(roots) == expected_roots, f"Incorrect roots of one for n={n}, alpha={alpha}"
    # Optionally check the length if the number of roots is known and should be specific
    assert len(roots) == len(expected_roots), f"Incorrect number of roots for n={n}, alpha={alpha}"

@pytest.mark.parametrize("generators, expected_products", [
    # Case 1: Testing with a simple list of IntricateInteger instances
    ([IntricateInteger(1, 7, 2), IntricateInteger(2, 7, 2)], {IntricateInteger(0, 7, 2)}),
    # Add more cases as needed
])
def test_generate_spanning_set(generators, expected_products):
    span_set = generate_spanning_set(generators)
    print(len(span_set),span_set)
    assert len(span_set) == len(expected_products), f"Expected set length {len(expected_products)}, got {len(span_set)}"
    
    # Check if every expected product is in the span_set
    for product in expected_products:
        assert product in span_set, f"Expected product {product} not found in spanning set"

####
#Parametrized tests from the second file for peculiar properties
@pytest.mark.parametrize("n, alpha, expected", [
    (7, 1, False),  # Assuming the property holds for these parameters
    (7, 6, True),  # Assuming the property does not hold for these parameters
    # The expected results here need to be aligned with the actual behavior of iterator_has_intricate_peculiar_property
])
def test_iterator_has_intricate_peculiar_property(n, alpha, expected):
    assert iterator_has_intricate_peculiar_property(n, alpha) == expected, f"Expected {expected} for n={n}, alpha={alpha}, got {result}"


@pytest.mark.parametrize("n, alpha, expected", [
    # Example cases: (n, alpha, expected_result)
    (3, 1, False),  # Assuming the associative property holds for these parameters
    (4, 1, False),  # Another hypothetical case where the property holds
    # You should adjust these test cases based on the actual behavior of your IntricateIntegers implementation
    # and the mathematical properties of the system you're modeling.
])
def test_iterator_has_associative_intricate_multiplication(n, alpha, expected):
    assert iterator_has_associative_intricate_multiplication(n, alpha) == expected, f"Failed for n={n}, alpha={alpha}"

@pytest.mark.parametrize("n, alpha, expected", [
    (3, 1, True),  # Assuming commutative property holds for these parameters
    (4, 1, True),  # Another hypothetical case where the property holds
    # You should adjust these test cases based on the actual behavior of your IntricateIntegers implementation
    # and the mathematical properties of the system you're modeling.
])
def test_iterator_has_commutative_intricate_multiplication(n, alpha, expected):
    assert iterator_has_commutative_intricate_multiplication(n, alpha) == expected, f"Commutative property test failed for n={n}, alpha={alpha}"


@pytest.mark.parametrize("n, alpha", [
    (3, 1),  # Example parameters where you expect your functions to operate correctly
    # Add more (n, alpha) tuples as necessary
])
def test_compare_times_runs(n, alpha):
    # Simply calling compare_times to ensure it runs without error
    # This doesn't verify timing output, but ensures the functions can be executed
    compare_times(n, alpha)


@pytest.mark.parametrize("n, alpha, expected", [
    (3, 1, False),  # Hypothetical case
    (1, 0, True),  # Hypothetical case
])
def test_has_intricate_peculiar_property(n, alpha, expected):
    assert has_intricate_peculiar_property(n, alpha) == expected, f"Test failed for n={n}, alpha={alpha}"

@pytest.mark.parametrize("n, alpha, expected", [
    (3, 1, True),  # Hypothetical case
    (4, 1, True),  # Hypothetical case
])
def test_has_commutative_intricate_multiplication(n, alpha, expected):
    assert has_commutative_intricate_multiplication(n, alpha) == expected, f"Test failed for n={n}, alpha={alpha}"

@pytest.mark.parametrize("n, alpha, expected", [
    (3, 1, False),  # Hypothetical case
    (4, 1, False),  # Hypothetical case
])
def test_has_associative_intricate_multiplication(n, alpha, expected):
    assert has_associative_intricate_multiplication(n, alpha) == expected, f"Test failed for n={n}, alpha={alpha}"

    
def test_intricate_integer_initialization():
    # Testing valid initialization
    obj = IntricateInteger(10, 7, 1)
    assert obj.value == 10 % 7
    assert obj.modulus == 7
    assert obj.alpha == 1

    # Testing modulus <= 0
    with pytest.raises(ValueError):
        IntricateInteger(10, 0, 1)
    
    # Testing alpha not in [0, modulus)
    with pytest.raises(ValueError):
        IntricateInteger(10, 7, -1)

def test_intricate_integer_str():
    obj = IntricateInteger(3, 7, 1)
    expected_str = "<3 mod 7 | 1>"
    assert str(obj) == expected_str


def test_intricate_integer_multiplication():
    obj1 = IntricateInteger(3, 7, 1)
    obj2 = IntricateInteger(4, 7, 1)
    result = obj1 * obj2
    expected_value = (3 + 4 + 1 * math.lcm(3, 4)) % 7
    assert result == IntricateInteger(expected_value, 7, 1)

    # Testing multiplication with incompatible objects
    with pytest.raises(ValueError):
        obj1 * IntricateInteger(4, 8, 1)  # different modulus

    with pytest.raises(ValueError):
        obj1 * "not an IntricateInteger"  # not an IntricateInteger instance

def test_intricate_integer_equality():
    obj1 = IntricateInteger(3, 7, 1)
    obj2 = IntricateInteger(3, 7, 1)
    obj3 = IntricateInteger(4, 7, 1)
    assert obj1 == obj2
    assert obj1 != obj3
    assert obj1 != "not an IntricateInteger"

def test_intricate_integer_hash():
    obj1 = IntricateInteger(3, 7, 1)
    obj2 = IntricateInteger(3, 7, 1)
    obj_set = {obj1, obj2}  # obj1 and obj2 should be considered equal and result in a set of length 1
    assert len(obj_set) == 1
    assert hash(obj1) == hash(obj2)

def test_intricate_integers_init_and_size():
    modulus, alpha = 5, 1
    set_of_integers = IntricateIntegers(modulus, alpha)
    
    # Verify the size method matches the modulus.
    assert set_of_integers.size() == modulus
    
    # Verify each element is an instance of IntricateInteger with correct modulus and alpha.
    for element in set_of_integers.elements:
        assert isinstance(element, IntricateInteger)
        assert element.modulus == modulus
        assert element.alpha == alpha

def test_intricate_integers_str():
    set_of_integers = IntricateIntegers(3, 2)
    expected_str = "{<0 mod 3 | 2>, <1 mod 3 | 2>, <2 mod 3 | 2>}"
    assert str(set_of_integers) == expected_str, "String representation does not match."

def test_value_error():
    print("Testing ValueError...")
    try:
        # Creating two IntricateInteger instances with different alpha values to trigger an exception
        int1 = IntricateInteger(1, 100, 10)  # Example instance with alpha=10
        int2 = IntricateInteger(2, 100, 20)  # Another instance with a different alpha=20
        result = int1 * int2  # Attempting multiplication should raise an exception due to mismatch
        assert False, "IntricateIntegerMismatch was not raised as expected."  # This line should not be executed
    except ValueError:
        print("ValueError raised successfully for incompatible IntricateIntegers.")  # Expected outcome

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

# This is commented out as although this is true - the test is skipped as the input set is empty.
# # Pytest parametrized test for checking the commutative property
# @pytest.mark.parametrize("commutative_results", icommutative_property_results, indirect=True)
# def test_commutative_property(commutative_results):
#     assert len(commutative_results) == 0  # Asserting that there are no results where the commutative property does not hold

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

