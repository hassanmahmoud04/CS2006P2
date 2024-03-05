import timeit
import pytest  # Added for pytest functionalities
from easy_medium_features import *
from i_integerwith_medium_features import *
from intricate_integer_hardfeatures import *
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers

from itertools import combinations

# Exception test for IntricateIntegerMismatch
def test_intricate_integer_mismatch():
    print("Testing IntricateIntegerMismatch exception...")
    try:
        int1 = IntricateInteger(1, 100, 10)  # Example instance
        int2 = IntricateInteger(2, 100, 20)  # Different alpha value
        result = int1 * int2  # This should raise IntricateIntegerMismatch
        assert False, "IntricateIntegerMismatch was not raised as expected."
    except IntricateIntegerMismatch:
        print("IntricateIntegerMismatch raised successfully for incompatible IntricateIntegers.")

# Common test function included from both versions
def test_intricate_integer():
    x = IntricateInteger(3, 7, 2)
    y = IntricateInteger(5, 7, 2)
    assert str(x) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x)}'"
    assert str(y) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(y)}'"
    assert str(x * x) == "<5 mod 7 | 2>", f"Expected '<5 mod 7 | 2>', got '{str(x * x)}'"
    assert str(x * y) == "<3 mod 7 | 2>", f"Expected '<3 mod 7 | 2>', got '{str(x * y)}'"
    try:
        z = IntricateInteger(1, 8, 3)  # Different modulus
        result = x * z
        assert False, "Expected ValueError for incompatible IntricateIntegers"
    except ValueError:
        pass  # Expected exception for incompatible operations
    print("IntricateInteger basic tests passed!")

# The function to generate results for peculiar and commutative properties
def peculiar_commutative_results():
    peculiar_property_results = []
    ipeculiar_property_results = []
    commutative_property_results = []
    icommutative_property_results = []
    for n in range(1, 51):
        peculiar_property_results += [(n, a) for a in range(0, n) if has_intricate_peculiar_property(n, a)]
        ipeculiar_property_results += [(n, a) for a in range(0, n) if iterator_has_intricate_peculiar_property(n, a)]
        commutative_property_results += [(n, a) for a in range(0, n) if not has_commutative_intricate_multiplication(n, a)]
        icommutative_property_results += [(n, a) for a in range(0, n) if not iterator_has_commutative_intricate_multiplication(n, a)]
    return peculiar_property_results, ipeculiar_property_results, commutative_property_results, icommutative_property_results

peculiar_property_results, ipeculiar_property_results, commutative_property_results, icommutative_property_results = peculiar_commutative_results()

# Parametrized tests from the second file for peculiar properties
@pytest.mark.parametrize("results_tuple", peculiar_property_results)
def test_peculiar_property(results_tuple):
    n, a = results_tuple
    assert a == n-1, f"{a} = {n-1}"

@pytest.mark.parametrize("results_tuple", ipeculiar_property_results)
def test_iterative_peculiar_property(results_tuple):
    n, a = results_tuple
    assert a == n-1, f"{a} = {n-1}"

# Fixture and test for commutative properties from the second file
@pytest.fixture
def commutative_results(request):  
    return request.param 

@pytest.mark.parametrize("commutative_results", commutative_property_results, indirect=True)
def test_commutative_property(commutative_results):
    assert len(commutative_results) == 0

# Testing new features included in both versions, ensuring no duplication
print("Testing associative property and intricate roots of one...")
for n in range(1, 6): # Example range, adjust as needed
    for alpha in range(0, n):
        print(f"n={n}, alpha={alpha}, associative: {has_associative_intricate_multiplication(n, alpha)}")
        print(f"n={n}, alpha={alpha}, roots of one: {intricate_roots_of_one(n, alpha)}")

w = IntricateInteger(3, 7, 2)
x = IntricateInteger(5, 7, 2)
y = IntricateInteger(6, 7, 2)
z = IntricateInteger(4, 7, 2)

span = generate_spanning_set([w, x, y, z])
for i in span:
    print(i)
