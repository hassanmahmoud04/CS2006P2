import timeit
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers
from i_integers_vhardfeatures import generate_spanning_set
from itertools import combinations


#intricate integer testing



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
commutativity_results = []
for n in range(1, 51):
    for alpha in range(n):
        peculiar_property = has_intricate_peculiar_property(n, alpha)
        commutativity = has_commutative_intricate_multiplication(n, alpha)
        if peculiar_property:
            peculiar_property_results.append((n, alpha))
        if not commutativity:
            commutativity_results.append((n, alpha))

print("Pairs (n, alpha) where x ⊗ x = x holds:", peculiar_property_results)
print("Pairs (n, alpha) where commutativity does not hold:", commutativity_results)

test_intricate_integer()

# intricate integers testing

peculiar_property_results = []
commutative_property_results = []

for n in range(1, 51):
    peculiar_property_results += [(n, a) for a in range(0, n) if iterator_has_intricate_peculiar_property(n, a)]
    commutative_property_results += [(n, a) for a in range(0, n) if iterator_has_commutative_intricate_multiplication(n, a)]

test_peculiar_property(peculiar_property_results)


print("Pairs (n, alpha) where commutativity does not hold:", commutative_property_results)



w = IntricateInteger(3, 7, 2)
x = IntricateInteger(5, 7, 2)
y = IntricateInteger(6, 7, 2)
z = IntricateInteger(4, 7, 2)

span = generate_spanning_set([w, x, y, z])
for i in span:
    print(i)