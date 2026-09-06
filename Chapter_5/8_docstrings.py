# Docstring: add information about function, class, module. It can be accessed by .__doc__


def sum(a, b):
    """
    this function returns sum of two numbers

    a (int): first number
    b (int): sencond number

    Returns:
    int: The sum of the numbers:
    """
    c = a + b
    return c


print(sum(3, 7))
print(sum.__doc__)
