# Import the IntricateInteger class from the intricate_integer module.
from intricate_integer import IntricateInteger

# Define a new class named IntricateIntegers.
class IntricateIntegers:
    # Initialize the IntricateIntegers object with modulus and alpha parameters.
    def __init__(self, modulus, alpha):
        # Store the modulus and alpha values in the object.
        self.modulus = modulus
        self.alpha = alpha
        # Create a list of IntricateInteger objects, one for each value from 0 to modulus-1,
        # all sharing the same modulus and alpha values.
        self.elements = [IntricateInteger(i, modulus, alpha) for i in range(modulus)]

    # Define the string representation of the IntricateIntegers object.
    def __str__(self):
        # Return a string that lists all IntricateInteger elements within curly braces,
        # separated by commas. This uses the __str__ method of the IntricateInteger class.
        return "{" + (", ".join(str(element) for element in self.elements)) + "}"

    # Make the IntricateIntegers object iterable, allowing it to be used in for loops.
    def __iter__(self):
        # Yield each element in the elements list one by one.
        for x in self.elements:
            yield x

    # Define a method to return the size of the IntricateIntegers set,
    # which is determined by the modulus.
    def size(self):
        # Return the modulus value, representing the number of elements in the set.
        return self.modulus
