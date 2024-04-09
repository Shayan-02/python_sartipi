def sums(a: float, b: float):
    """
    Sum tow number that input from user.

    Args:
        a (float): the first number.
        b (float): the second number.

    Returns:
        c (float): the sum of a and b.
    """
    c = a + b
    print(c)
    
x = lambda a : a + 10
print(x(5))

def myfunc(n):
      return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

