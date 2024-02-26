from intricate_integer import IntricateInteger
import math

class IntricateIntegers:
    def __init__(self, modulus, alpha):
        self.modulus = modulus
        self.alpha = alpha
        self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    def __str__(self):
        return "{"+(", ".join(str(element) for element in self.elements))+"}"

    def __iter__(self):
        for x in self.elements:
            yield x

    def size(self):
        return self.modulus

intricate_integers = IntricateIntegers(7, 2)
print(intricate_integers)
print(intricate_integers.size())

# check whether or not x ⊗ x = x holds for all x ∈ Zn
def iterator_has_intricate_peculiar_property(n,alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for elem in intricate_integers:
        if (elem * elem).value != elem.value:
            return False
    return True

# check for all pairs (n, α), where 1 ≤ n ≤ 50 and 0 ≤ α < n, that this property holds if and only if α = n − 1.
def test_peculiar_property(peculiarity_results):
    for n, a in peculiarity_results:
        if a != n-1:
            print("Test failed: property does not hold for",(n, a))
            return
    print("Test passed! property holds if and only if α = n − 1")

# check whether or not x ⊗ y = y ⊗ x  holds for all x ∈ Zn
def iterator_has_commutative_intricate_multiplication(n,alpha):
    intricate_integers = IntricateIntegers(n, alpha)

    for i, elem in enumerate(intricate_integers, 0):
        for j, elem2 in enumerate(intricate_integers, 1): # Start from x+1 to avoid redundant checks
            if (elem * elem2).value != (elem2 * elem).value:
                return False
    return True

# New feature: Check associative property
def has_associative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for x in intricate_integers:
        for y in intricate_integers:
            for z in intricate_integers:
                if not (((x * y) * z).value == (x * (y * z)).value):
                    return False
    return True

# New feature: Find intricate roots of one
def intricate_roots_of_one(n, alpha):
    roots = []
    for x in range(n):
        elem = IntricateInteger(x, n, alpha)
        if (elem * elem).value == IntricateInteger(1, n, alpha).value:
            roots.append(x)
    return roots

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
