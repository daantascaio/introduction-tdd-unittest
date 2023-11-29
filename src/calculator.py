def sum(x, y):
    """Sum x and y

    >>> sum(10, 20)
    30

    >>> sum(20, -5)
    15

    >>> sum(0, 20)
    20

    >>> sum(-22, -20)
    -42

    >>> sum(10.5, 20.5)
    31.0

    >>> sum(-10.5, -20.5)
    -31.0

    >>> sum(-10.5, 20.5)
    10.0

    # >>> sum('-10.5', 20)
    # Traceback (most recent call last):
    # ...
    # AssertionError: x need is int or float
    """
    assert isinstance(x, (int, float)), 'x need a int or float'
    assert isinstance(y, (int, float)), 'y need a int or float'

    return x + y


def subtrai(x, y):
    """Subtrai x and y

    >>> subtrai(10, 5)
    5

    >>> subtrai('5', 10)
    # Traceback (most recent call last):
    # ...
    # AssertionError: x need is int or float
    """
    assert isinstance(x, (int, float)), 'x need a int or float'
    assert isinstance(y, (int, float)), 'y need a int or float'

    return x - y


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
