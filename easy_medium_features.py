# Import the IntricateInteger and IntricateIntegers classes from their respective modules.
from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers

# Define a function to check if all elements in a set have the peculiar property
# where squaring the element results in the element itself.
def has_intricate_peculiar_property(n, alpha):
    # Iterate over all possible values within the modulus range.
    for x in range(n):
        # Create an IntricateInteger instance with the current value, modulus, and alpha.
        ix = IntricateInteger(x, n, alpha)
        # Check if squaring the element does not result in the element itself.
        if (ix * ix).value != ix.value:
            return False  # If any element fails the check, return False immediately.
    return True  # If all elements pass the check, return True.

# Define a function to check if the commutative property holds for multiplication
# among all pairs of elements in the set.
def has_commutative_intricate_multiplication(n, alpha):
    # Iterate over all pairs of distinct elements within the modulus range.
    for x in range(n):
        for y in range(x + 1, n):  # Start from x+1 to ensure y > x and avoid redundant checks.
            # Create IntricateInteger instances for each element in the pair.
            ix = IntricateInteger(x, n, alpha)
            iy = IntricateInteger(y, n, alpha)
            # Check if the product of the pair in both orders results in different values.
            if (ix * iy).value != (iy * ix).value:
                return False  # If any pair fails the check, return False immediately.
    return True  # If all pairs pass the check, return True.

# Define a function to check if the associative property holds for multiplication
# among all triplets of elements in the set.
def has_associative_intricate_multiplication(n, alpha):
    # Iterate over all possible triplets of elements within the modulus range.
    for x in range(n):
        for y in range(n):
            for z in range(n):
                # Calculate the product of the first two elements, and then the last two elements.
                xy = IntricateInteger(x, n, alpha) * IntricateInteger(y, n, alpha)
                yz = IntricateInteger(y, n, alpha) * IntricateInteger(z, n, alpha)
                # Check if the associative property does not hold for the triplet.
                if (xy * IntricateInteger(z, n, alpha)).value != (IntricateInteger(x, n, alpha) * yz).value:
                    return False  # If any triplet fails the check, return False immediately.
    return True  # If all triplets pass the check, return True.
