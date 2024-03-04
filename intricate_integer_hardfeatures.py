from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers
from itertools import combinations

# Hard: Find intricate roots of one
def intricate_roots_of_one(n, alpha):
    roots = []
    for x in range(n):
        elem = IntricateInteger(x, n, alpha)
        if (elem * elem).value == IntricateInteger(1, n, alpha).value:
            roots.append(x)
    return roots

# Very hard:
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
