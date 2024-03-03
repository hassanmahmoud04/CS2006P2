import math
import numpy as np
from itertools import combinations

class IntricateInteger:
    def __init__(self, obj, modulus, alpha):
        self.value = obj
        self.modulus = modulus
        self.alpha = alpha
        ##self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    def __str__(self):
        ##return "{"+(", ".join(str(element) for element in self.elements))+"}"
        return f"<{self.value} mod {self.modulus} | {self.alpha}>"

    def size(self):
        return self.modulus
    def __mul__(self,other):
        if self.modulus != other.modulus:
            raise IntricateIntegerMismatch
        if self.alpha != other.alpha:
            raise IntricateIntegerMismatch
        obj = (self.value+other.value + self.alpha * math.lcm(self.value,other.value)) % self.modulus
        return IntricateInteger(obj,self.modulus,self.alpha)
    def __eq__(self, other):
        # Check if 'other' is instance of MyClass and compare values
        return isinstance(other, IntricateInteger) and self.value == other.value and self.modulus == other.modulus and self.alpha == other.alpha
    def __hash__(self):
        return hash(self.value)

class IntricateIntegers:
    def __init__(self, modulus, alpha):
        self.modulus = modulus
        self.alpha = alpha
        self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    def __str__(self):
        return ", ".join(str(element) for element in self.elements)

    def size(self):
        return len(self.elements)
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        if self.current < self.size():
            result = self.elements[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

def generate_spanning_set(generators):
    all_combinations = []
    product_combo = set()

    # Generate combinations for every possible length
    for r in range(1, len(generators) + 1):
        # Extend the list with combinations of the current length
        all_combinations.extend(combinations(generators, r))
    for d in all_combinations:
        if len(d) > 1:
            product = d[0]

            for i in range(1,len(d)):
                m = d[i]
                product = product * m
            product_combo.add(product)
    return product_combo

# generators = (IntricateInteger(3, 9, 6), IntricateInteger(2, 9, 6), IntricateInteger(5, 9, 6), IntricateInteger(8, 9, 6))
# span_set = generate_spanning_set(generators)

# for i in span_set:
#     print(i)
