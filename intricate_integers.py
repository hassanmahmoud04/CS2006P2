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