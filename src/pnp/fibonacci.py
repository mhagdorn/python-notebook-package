def fibonacci(n: int) -> int:
    """generator producing Fibonacci numbers

    :param n: the number of Fibonnaci numbers to produce,
              must be greater than 0
    :type n: int
    """
    if n < 1:
        raise ValueError("n must be greater than 0")
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
