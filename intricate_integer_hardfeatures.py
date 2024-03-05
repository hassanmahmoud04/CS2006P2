# Import the IntricateInteger class from the intricate_integer module.
from intricate_integer import IntricateInteger
# Import the IntricateIntegers class from the intricate_integers module.
from intricate_integers import IntricateIntegers
# Import the combinations function from the itertools module to generate combinations of elements.
from itertools import combinations

# Define a function to find the intricate roots of one for a given modulus n and parameter alpha.
def intricate_roots_of_one(n, alpha):
    roots = []  # Initialize an empty list to store the roots.
    for x in range(n):  # Iterate over all possible values of x within the modulus range.
        elem = IntricateInteger(x, n, alpha)  # Create an IntricateInteger instance with the current x, modulus n, and alpha.
        # Check if squaring the element results in an IntricateInteger equal to 1 (mod n) with the same alpha.
        if (elem * elem).value == IntricateInteger(1, n, alpha).value:
            roots.append(x)  # If the condition is met, append x to the list of roots.
    return roots  # Return the list of roots.

# Define a function to generate a spanning set from a list of generator IntricateInteger instances.
def generate_spanning_set(generators):
    all_combinations = []  # Initialize an empty list to store all combinations of the generator elements.
    product_combo = set()  # Initialize an empty set to store unique products of combinations.

    # Generate combinations for every possible length from 1 to the length of the generator list.
    for r in range(1, len(generators) + 1):
        # Extend the list with all combinations of length r.
        all_combinations.extend(combinations(generators, r))

    # Iterate over each combination of generator elements.
    for d in all_combinations:
        if len(d) > 1:  # Check if the combination has more than one element.
            product = d[0]  # Initialize the product with the first element of the combination.

            # Multiply each subsequent element in the combination with the product.
            for i in range(1,len(d)):
                m = d[i]  # Get the next element in the combination.
                product = product * m  # Update the product by multiplying it with the current element.
            product_combo.add(product)  # Add the final product to the set of unique products.

    return product_combo  # Return the set of unique products as the spanning set.
