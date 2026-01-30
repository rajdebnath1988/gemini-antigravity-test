def fibonacci(n):
    """
    Calculates the Fibonacci sequence up to the nth term.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence