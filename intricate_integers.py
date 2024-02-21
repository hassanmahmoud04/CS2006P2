from intricate_integer import IntricateInteger

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


def iterator_has_commutative_intricate_multiplication(n,alpha):
    intricate_integers = IntricateIntegers(n, alpha) 
    for elem in intricate_integers:


peculiar_property_results = []
not_commutativity_results = []

for n in range(1, 51):
    for a in range(0, n):
        if iterator_has_intricate_peculiar_property(n, a):
            peculiar_property_results.append((n, a))
        # if not iterator_has_commutative_intricate_multiplication(n, a):
        #     commutativity_results.append((n, a))

print("Pairs (n, alpha) where x ⊗ x = x holds:", peculiar_property_results)

                