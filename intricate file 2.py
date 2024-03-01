from intricate_integer_hardfeatures import IntricateInteger
from intricate_integer_hardfeatures import iterator_has_intricate_peculiar_property, iterator_has_commutative_intricate_multiplication, has_associative_intricate_multiplication, intricate_roots_of_one

import math

# check for all pairs (n, α), where 1 ≤ n ≤ 50 and 0 ≤ α < n, that this property holds if and only if α = n − 1.
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