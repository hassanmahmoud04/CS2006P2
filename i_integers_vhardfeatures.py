# Import necessary libraries
import math  # For mathematical operations such as least common multiple (lcm)
import numpy as np  # For numerical operations, though it's not used in the provided snippet
from itertools import combinations  # For generating combinations of elements

# Define the IntricateInteger class
class IntricateInteger:
    # Define a custom exception for handling mismatches in IntricateInteger operations
    class IntricateIntegerMismatch(Exception):
        def __init__(self, message="Intricate integer properties mismatch"):
            self.message = message  # Custom message for the exception
            super().__init__(self.message)  # Initialize the base Exception class with the custom message

    # Initialize an IntricateInteger instance with value (obj), modulus, and alpha
    def __init__(self, obj, modulus, alpha):
        self.value = obj  # The integer value of the instance
        self.modulus = modulus  # The modulus value for modulo operations
        self.alpha = alpha  # The alpha value, a parameter that influences multiplication behavior

    # String representation of an IntricateInteger instance
    def __str__(self):
        return f"<{self.value} mod {self.modulus} | {self.alpha}>"

    # Return the size of the IntricateInteger set, equivalent to the modulus value
    def size(self):
        return self.modulus

    # Define the multiplication operation between two IntricateInteger instances
    def __mul__(self, other):
        # Check for matching modulus and alpha values before multiplication, raise exception if mismatched
        if self.modulus != other.modulus or self.alpha != other.alpha:
            raise IntricateIntegerMismatch
        # Calculate the new value after multiplication, ensuring it's within the modulus
        obj = (self.value + other.value + self.alpha * math.lcm(self.value, other.value)) % self.modulus
        # Return a new IntricateInteger instance with the calculated value
        return IntricateInteger(obj, self.modulus, self.alpha)

    # Define equality comparison for two IntricateInteger instances
    def __eq__(self, other):
        # True if both instances have the same value, modulus, and alpha; False otherwise
        return isinstance(other, IntricateInteger) and self.value == other.value and self.modulus == other.modulus and self.alpha == other.alpha

    # Define the hash function for an IntricateInteger instance to allow its use in sets and dictionaries
    def __hash__(self):
        return hash(self.value)

# Define the IntricateIntegers class for handling a set of IntricateInteger instances
class IntricateIntegers:
    # Initialize an IntricateIntegers instance with a modulus and alpha
    def __init__(self, modulus, alpha):
        self.modulus = modulus  # The modulus value for the set
        self.alpha = alpha  # The alpha value for the set
        # Create a list of IntricateInteger instances for each value from 0 to modulus-1
        self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    # String representation of an IntricateIntegers instance
    def __str__(self):
        return ", ".join(str(element) for element in self.elements)

    # Return the size of the IntricateIntegers set, which is the number of elements
    def size(self):
        return len(self.elements)
    
    # Define the iterator protocol for IntricateIntegers to allow iteration
    def __iter__(self):
        self.current = 0  # Initialize the current position for iteration
        return self
    
    # Define the next item to return during iteration
    def __next__(self):
        # Check if the current position is within the bounds of the elements list
        if self.current < self.size():
            result = self.elements[self.current]  # Retrieve the current element
            self.current += 1  # Move to the next position
            return result  # Return the current element
        else:
            raise StopIteration  # End iteration if beyond the last element

# Define a function to generate a spanning set from a list of generator IntricateInteger instances
def generate_spanning_set(generators):
    all_combinations = []  # List to hold all possible combinations of generators
    product_combo = set()  # Set to hold unique products of combinations

    # Generate combinations for every possible length
    for r in range(1, len(generators) + 1):
        all_combinations.extend(combinations(generators, r))  # Add combinations of length r to the list
    for d in all_combinations:
        if len(d) > 1:  # If the combination has more than one element
            product = d[0]  # Start with the first element as the initial product
            for i in range(1, len(d)):  # Iterate through the rest of the elements
                m = d[i]  # Get the current element
                product = product * m  # Multiply the product by the current element
            product_combo.add(product)  # Add the final product to the set of unique products
    return product_combo  # Return the set of unique products as the spanning set
