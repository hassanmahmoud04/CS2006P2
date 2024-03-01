import math

class IntricateInteger:
    def __init__(self, obj, modulus, alpha):
        self.value = obj
        self.modulus = modulus
        self.alpha = alpha
        ##self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    def __str__(self):
        ##return "{"+(", ".join(str(element) for element in self.elements))+"}"
        return str(self.value)+" "+str(self.modulus)+" "+str(self.alpha)

    def size(self):
        return self.modulus
    def __mul__(self,other):
        if self.modulus != other.modulus:
            raise IntricateIntegerMismatch
        if self.alpha != other.alpha:
            raise IntricateIntegerMismatch
        obj = (self.value+other.value + self.alpha * math.lcm(self.value,other.value)) % self.modulus
        return IntricateInteger(obj,self.modulus,self.alpha)

class IntricateIntegerIterator:
    def __init__(self, intricate_instance):
        self.current = intricate_instance.value  # Start iteration from 0
        self.end = intricate_instance.modulus  # End of iteration defined by n
        self.alpha = intricate_instance.alpha
    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            # Create a new instance of A for the current value
            instance = IntricateInteger(self.current,self.end,self.alpha)
            self.current += 1
            return instance
        else:
            raise StopIteration

intricate_integers = IntricateInteger(3, 7, 2)
print(intricate_integers)
print(intricate_integers.size())

# check whether or not x ⊗ x = x holds for all x ∈ Zn
def iterator_has_intricate_peculiar_property(n,alpha):
    intricate_integers = IntricateInteger(0, n, alpha)
    iterator = IntricateIntegerIterator(intricate_integers)
    for elem in iterator:
        if (elem * elem).value != elem.value:
            return False
    return True


# check whether or not x ⊗ y = y ⊗ x  holds for all x ∈ Zn
def iterator_has_commutative_intricate_multiplication(n,alpha):
    intricate_integers = IntricateInteger(0, n, alpha)
    # Create an iterator using the initial_instance
    iterator = IntricateIntegerIterator(intricate_integers)
    ##iterator = IntricateIterator(intricate_integers)

    # Iterate and print the value of n for each new instance of A
    for elem in iterator:
        iteratorb = IntricateIntegerIterator(IntricateInteger(elem.value,n,alpha))
        for elem2 in iteratorb:

    ##for i, elem in enumerate(intricate_integers, 0):
        ##for j, elem2 in enumerate(intricate_integers, 1): # Start from x+1 to avoid redundant checks
            if (elem * elem2).value != (elem2 * elem).value:
                return False
    return True

# New feature: Check associative property
def has_associative_intricate_multiplication(n, alpha):
    ##intricate_integers = IntricateInteger(n, alpha)
    intricate_integers = IntricateInteger(0, n, alpha)
    iteratorx = IntricateIntegerIterator(intricate_integers)
    for x in iteratorx:
        iteratory = IntricateIntegerIterator(intricate_integers)
        for y in iteratory:
            iteratorz = IntricateIntegerIterator(intricate_integers)
            for z in iteratorz:
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

