import math

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

    def __eq__(self, other):
        # Check if 'other' is instance of MyClass and compare values
        return isinstance(other, IntricateInteger) and self.value == other.value and self.modulus == other.modulus and self.alpha == other.alpha
    def __hash__(self):
        return hash(self.value)

