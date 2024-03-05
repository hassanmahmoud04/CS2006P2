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

def valid_associative_pairs():
    associativity_results = []
    iassociativity_results = []

    for n in range(1, 21):
        associativity_results += [(n, a) for a in range(0, n) if has_associative_intricate_multiplication(n, a)]
        iassociativity_results += [(n, a) for a in range(0, n) if iterator_has_associative_intricate_multiplication(n, a)]

    if ((len(associativity_results) == 210) and (len(iassociativity_results) == 210)):
        print("associativity holds for all 1≤n≤20 and 0≤a<n.")
    else:
        print("Pairs (n, alpha) where associativity holds:", associativity_results)

valid_associative_pairs()


""" get results ready to use for unit testing """
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
    assert a == n-1, f"{a} = {n-1} holds for all pairs (n,a), where 1≤n≤50 and 0≤a<n."


""" Parametrized tests to make sure a = n-1 hold for all pairs (n, alpha) where 1 <= n <= 50 and 0 <= alpha < n """
@pytest.mark.parametrize("results_tuple", ipeculiar_property_results)
def test_iterative_peculiar_property(results_tuple):
    n, a = results_tuple
    assert a == n-1, f"{a} = {n-1} for for all pairs (n,a), where 1≤n≤50 and 0≤a<n."

""" tests to check whether commutativity holds for all pairs (n,a), where 1≤n≤50 and 0≤a<n """
def test_commutative_property():
    commutative_results = commutative_property_results

    assert not commutative_results, f"commutativity holds for all pairs (n,a), where 1≤n≤50 and 0≤a<n. "
    

def test_iterative_commutative_property():
    commutative_results = icommutative_property_results

    assert not commutative_results, f"commutativity holds for all pairs (n,a), where 1≤n≤50 and 0≤a<n. "
    