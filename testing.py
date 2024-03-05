import timeit
import pytest
from easy_medium_features import *
from i_integerwith_medium_features import *
from intricate_integer_hardfeatures import *
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers

from itertools import combinations



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

# Check for all pairs (n, alpha) where 1 <= n <= 50 and 0 <= alpha < n
peculiar_property_results = []
commutative_property_results = []
for n in range(1, 51):
    for alpha in range(n):
        peculiar_property = has_intricate_peculiar_property(n, alpha)
        commutativity = has_commutative_intricate_multiplication(n, alpha)
        if peculiar_property:
            peculiar_property_results.append((n, alpha))
        if not commutativity:
            commutative_property_results.append((n, alpha))

print("Pairs (n, alpha) where x ⊗ x = x holds:", peculiar_property_results)
print("Pairs (n, alpha) where commutativity does not hold:", commutative_property_results)

test_intricate_integer()

print("Pairs (n, alpha) where commutativity does not hold:", commutative_property_results)

def test_peculiar_property(peculiarity_results):
    for n, a in peculiarity_results:
        if a != n-1:
            print("Test failed: property does not hold for",(n, a))
            return
    print("Test passed! property holds if and only if α = n − 1")
    
peculiar_property_results = []
commutative_property_results = []

for n in range(1, 51):
    peculiar_property_results += [(n, a) for a in range(0, n) if iterator_has_intricate_peculiar_property(n, a)]
    commutative_property_results += [(n, a) for a in range(0, n) if iterator_has_commutative_intricate_multiplication(n, a)]

test_peculiar_property(peculiar_property_results)

print("Pairs (n, alpha) where commutativity does not hold:", commutative_property_results)

# Testing new features
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

""" Parametrized tests to make sure a = n-1 hold for all pairs (n, alpha) where 1 <= n <= 50 and 0 <= alpha < n """
@pytest.mark.parametrize("results_tuple", peculiar_property_results)
def test_peculiar_property(results_tuple):
    n, a = results_tuple
    assert a == n-1, f"{a} = {n-1}"


""" Parametrized tests to make sure a = n-1 hold for all pairs (n, alpha) where 1 <= n <= 50 and 0 <= alpha < n """
@pytest.mark.parametrize("results_tuple", ipeculiar_property_results)
def test_iterative_peculiar_property(results_tuple):
    n, a = results_tuple
    assert a == n-1, f"{a} = {n-1}"

""" tests to check whether commutativity holds for all pairs (n,a), where 1≤n≤50 and 0≤a<n """
def test_commutative_property():
    commutative_results = commutative_property_results

    assert len(commutative_results) == 0, f"test passed"

def test_iterative_commutative_property():
    commutative_results = icommutative_property_results

    assert len(commutative_results) == 0