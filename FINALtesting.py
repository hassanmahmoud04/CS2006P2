import timeit
import pytest  # Added for pytest functionalities
from easy_medium_features import *
from i_integerwith_medium_features import *
from intricate_integer_hardfeatures import *
from intricate_integer import IntricateInteger, IntricateIntegerMismatch
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
    with pytest.raises(IntricateIntegerMismatch):
        IntricateInteger(10, 0, 1)
    
    # Testing alpha not in [0, modulus)
    with pytest.raises(IntricateIntegerMismatch):
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
    with pytest.raises(IntricateIntegerMismatch):
        obj1 * IntricateInteger(4, 8, 1)  # different modulus

    with pytest.raises(IntricateIntegerMismatch):
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


# # Common test function included from both versions
# #def test_intricate_integer():
#     #x = IntricateInteger(3, 7, 2)
#     #y = IntricateInteger(5, 7, 2)
#     #assert str(x) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x)}'"
#     #assert str(y) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(y)}'"
#     #assert str(x * x) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(x * x)}'"
#     #assert str(x * y) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x * y)}'"
#     #try:
#     #    z = IntricateInteger(1, 8, 3)  # Different modulus
#     #    result = x * z
#     #    assert False, "Expected ValueError for incompatible IntricateIntegers"
#     #except ValueError:
#     #    pass  # Expected exception for incompatible operations
#     #print("IntricateInteger basic tests passed!")



# # The function to generate results for peculiar and commutative properties
# @pytest.mark.parametrize("n, alpha, expected", [
#     # Example cases: (n, alpha, expected_result)
#     # Note: The expected results here need to be manually verified or correctly determined for each case.
#     (7, 1, True),  # Assuming the peculiar property holds for these parameters
#     (7, 6, False),  # Assuming the peculiar property does not hold for these parameters
#     # Add more cases as necessary
# ])
# def test_iterator_has_intricate_peculiar_property(n, alpha, expected):
#     assert iterator_has_intricate_peculiar_property(n, alpha) == expected, f"Failed for n={n}, alpha={alpha}"



# @pytest.mark.parametrize("results_tuple", peculiar_property_results)
# def test_iterative_peculiar_property(results_tuple):
#     n, a = results_tuple
#     assert a == n-1, f"{a} = {n-1}"

# # Fixture and test for commutative properties from the second file
# @pytest.fixture
# def commutative_results(request):  
#     return request.param 

# @pytest.mark.parametrize("commutative_results", commutative_property_results, indirect=True)
# def test_commutative_property(commutative_results):
#     assert len(commutative_results) == 0

# # Testing new features included in both versions, ensuring no duplication


# #@pytest.mark.parametrize("value1, modulus1, alpha1, value2, modulus2, alpha2", [
#     (1, 100, 10, 2, 100, 20),  # Example case
# #])
# #def test_intricate_integer_mismatch(value1, modulus1, alpha1, value2, modulus2, alpha2):
#     #int1 = IntricateInteger(value1, modulus1, alpha1)
#     #int2 = IntricateInteger(value2, modulus2, alpha2)
    
#     #with pytest.raises(IntricateIntegerMismatch, match="IntricateIntegerMismatch was not raised as expected."):
#     #    result = int1 * int2

# @pytest.mark.parametrize("value1, modulus1, alpha1, value2, modulus2, alpha2", [
#     (1, 100, 10, 2, 100, 20),  # Example case
# ])
# def test_intricate_integer_mismatch(value1, modulus1, alpha1, value2, modulus2, alpha2):
#     int1 = IntricateInteger(value1, modulus1, alpha1)
#     int2 = IntricateInteger(value2, modulus2, alpha2)
    
#     with pytest.raises(IntricateIntegerMismatch, match="IntricateIntegerMismatch was not raised as expected."):
#         result = int1 * int2



