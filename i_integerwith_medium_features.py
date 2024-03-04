import math
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers

def iterator_has_intricate_peculiar_property(n,alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for elem in intricate_integers:
        if (elem * elem).value != elem.value:
            return False
    return True

##############################################
def has_associative_intricate_multiplication(n, alpha):
    for x in IntricateIntegers(n,alpha):
        for y in x:
            for z in y:
                if not (((x * y) * z).value == (x * (y * z)).value):
                    return False
    return True

def iterator_has_commutative_intricate_multiplication(n, alpha):
    intricate_integeres = IntricateIntegers(n, alpha)

    for i, elem in enumerate(intricate_integeres):
        for j, elem2 in intricate_integeres:
            if not ((elem * elem2).value == (elem2 * elem).value):
                return False
    return True

associativity_results = []
for n in range(1, 21):
    for alpha in range(n):
        if has_associative_intricate_multiplication(n, alpha):
            associativity_results.append((n, alpha))

print("Pairs (n, alpha) where associativity holds:", associativity_results)

# Testing the IntricateIntegers class and iteration
intricate_set = IntricateIntegers(3, 2)
print("IntricateIntegers(3, 2):")
for x in intricate_set:
    print(x)
