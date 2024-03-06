# Import the math module for mathematical functions.
import math

# Define a new class named IntricateInteger.
class IntricateInteger:
    # Initialize the IntricateInteger object with value, modulus, and alpha parameters.
    def __init__(self, value, modulus, alpha):
        # Validate that the modulus is a positive integer.
        if not (0 <= value < modulus):
            raise ValueError("Value must be in the set {0, 1, ..., modulus - 1}")
        if modulus <= 0:
            raise ValueError("Modulus must be a positive integer")
        # Validate that alpha is within the valid range [0, modulus).
        if not (0 <= alpha < modulus):
            raise ValueError("Alpha must be in the set {0, 1, ..., modulus - 1}")
        # Set the value of the IntricateInteger, ensuring it is within the range [0, modulus) using modulus operation.
        self.value = value % modulus
        # Store the modulus and alpha values in the object.
        self.modulus = modulus
        self.alpha = alpha

    # Define the string representation of the IntricateInteger object.
    def __str__(self):
        # Return a formatted string showing the value, modulus, and alpha of the IntricateInteger.
        return f"<{self.value} mod {self.modulus} | {self.alpha}>"

    # Define the multiplication operation between two IntricateInteger instances.
    def __mul__(self, other):
        # Ensure that the other operand is also an IntricateInteger instance.
        if not isinstance(other, IntricateInteger):
            raise ValueError("Can only multiply IntricateInteger instances")
        # Check if the modulus and alpha values are compatible between the two IntricateInteger instances.
        if self.modulus != other.modulus or self.alpha != other.alpha:
            raise ValueError("Incompatible IntricateIntegers: different modulus or alpha")
        # Calculate the new value according to the specified formula, ensuring it falls within the modulus range.
        new_value = (self.value + other.value + self.alpha * math.lcm(self.value, other.value)) % self.modulus
        # Return a new IntricateInteger instance with the calculated value, preserving the modulus and alpha.
        return IntricateInteger(new_value, self.modulus, self.alpha)

    # Define equality comparison between two IntricateInteger instances.
    def __eq__(self, other):
        # Return True if the other instance is an IntricateInteger with matching value, modulus, and alpha; False otherwise.
        return isinstance(other, IntricateInteger) and self.value == other.value and self.modulus == other.modulus and self.alpha == other.alpha

    # Define the hash function for IntricateInteger, allowing it to be used in sets and as dictionary keys.
    def __hash__(self):
        # Use the hash of the value for the hash implementation.
        return hash(self.value)
