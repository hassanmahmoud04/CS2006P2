import math

def lcm(x, y):
    return abs(x*y) // math.gcd(x, y) if x and y else 0

class IntricateInteger:
    def __init__(self, value, modulus, alpha):
        if modulus <= 0:
            raise ValueError("Modulus must be a positive integer")
        if not (0 <= alpha < modulus):
            raise ValueError("Alpha must be in the set {0, 1, ..., modulus - 1}")
        self.value = value % modulus
        self.modulus = modulus
        self.alpha = alpha

    def __str__(self):
        return f"<{self.value} mod {self.modulus} | {self.alpha}>"

    def __mul__(self, other):
        if not isinstance(other, IntricateInteger):
            raise ValueError("Can only multiply IntricateInteger instances")
        if self.modulus != other.modulus or self.alpha != other.alpha:
            raise ValueError("Incompatible IntricateIntegers: different modulus or alpha")
        new_value = (self.value + other.value + self.alpha * math.lcm(self.value, other.value)) % self.modulus
        return IntricateInteger(new_value, self.modulus, self.alpha)

def has_intricate_peculiar_property(n, alpha):
    for x in range(n):
        ix = IntricateInteger(x, n, alpha)
        if (ix * ix).value != ix.value:
            return False
    return True

def has_commutative_intricate_multiplication(n, alpha):
    for x in range(n):
        for y in range(x + 1, n):  # Start from x+1 to avoid redundant checks
            ix = IntricateInteger(x, n, alpha)
            iy = IntricateInteger(y, n, alpha)
            if (ix * iy).value != (iy * ix).value:
                return False
    return True

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
