from intricate_integer import IntricateInteger
from intricate_integers import IntricateIntegers

def has_intricate_peculiar_property(n, alpha):
    for x in range(n):
        ix = IntricateInteger(x, n, alpha)
        if (ix * ix).value != ix.value:
            return False
    return True

def has_commutative_intricate_multiplication(n, alpha):
    for x in range(n):
        for y in range(x + 1, n):  # Start from x+1 to avoid redundant checks
            ix = IntricateInteger(x, n, alpha)
            iy = IntricateInteger(y, n, alpha)
            if (ix * iy).value != (iy * ix).value:
                return False
    return True

def has_associative_intricate_multiplication(n, alpha):
    for x in range(n):
        for y in range(n):
            for z in range(n):
                xy = IntricateInteger(x, n, alpha) * IntricateInteger(y, n, alpha)
                yz = IntricateInteger(y, n, alpha) * IntricateInteger(z, n, alpha)
                if (xy * IntricateInteger(z, n, alpha)).value != (IntricateInteger(x, n, alpha) * yz).value:
                    return False
    return True