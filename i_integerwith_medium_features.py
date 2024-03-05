import math
import timeit
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers
from easy_medium_features import *

def iterator_has_intricate_peculiar_property(n,alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for elem in intricate_integers:
        if (elem * elem).value != elem.value:
            return False
    return True

##############################################
def iterator_has_associative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)

    for x in IntricateIntegers(n,alpha):
        for y in IntricateIntegers(n,alpha):
            for z in IntricateIntegers(n,alpha):
                if not (((x * y) * z).value == (x * (y * z)).value):
                    return False
    return True

def iterator_has_commutative_intricate_multiplication(n, alpha):
    intricate_integeres = IntricateIntegers(n, alpha)

    for i, elem in enumerate(intricate_integeres, 0):
        for j, elem2 in enumerate(intricate_integeres, 1):
            if not ((elem * elem2).value == (elem2 * elem).value):
                return False
    return True

associativity_results = []
for n in range(1, 21):
    for alpha in range(n):
        if iterator_has_associative_intricate_multiplication(n, alpha):
            associativity_results.append((n, alpha))

print("Pairs (n, alpha) where associativity holds:", associativity_results)

# Testing the IntricateIntegers class and iteration
intricate_set = IntricateIntegers(3, 2)
print("IntricateIntegers(3, 2):")
for x in intricate_set:
    print(x)

def compare_times(n, alpha):
    iterator_assoc = timeit.timeit(lambda: iterator_has_associative_intricate_multiplication(n, alpha), number=10000)
    loop_assoc = timeit.timeit(lambda: has_associative_intricate_multiplication(n, alpha), number=10000)
    print("Time for 10000 tests for iterator associativity: " + str(iterator_assoc))
    print("Time for 10000 tests for for loop associativity: " + str(loop_assoc))
    print("Difference: " + str(abs(loop_assoc - iterator_assoc)))

    iterator_commut = timeit.timeit(lambda: iterator_has_commutative_intricate_multiplication(n, alpha), number=10000)
    loop_commut = timeit.timeit(lambda: has_commutative_intricate_multiplication(n, alpha), number=10000)
    print("Time for 10000 tests for iterator commutativity: " + str(iterator_commut))
    print("Time for 10000 tests for for loop commutativity: " + str(loop_commut))
    print("Difference: " + str(abs(loop_commut - iterator_commut)))

print("Comparing times for (3,2):")
compare_times(3, 2)
