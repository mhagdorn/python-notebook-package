def fibonacci(n: int) -> int:
    if n < 1:
        raise ValueError("n must be greater than 0")
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
