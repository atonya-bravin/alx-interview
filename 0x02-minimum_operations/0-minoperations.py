"""#!/usr/bin/python3

This a module that contains a solution to an interview question.
The question requires that we write a method that calculates the
fewest number of operations needed to result in exactly n H characters
in a file that accepts only two operations.
- CopyAll
- Paste
"""


def minOperations(n: int) -> int:
    """
    This function takes in an integer and calculates the number of
    operations needed to result in exactly n H characters.
    """

    if type(n) != int:
        return 0

    if n == 2 or n == 3:
        return n

    elif n % 3 == 0:
        return 3 + int((n / 3))

    elif n % 2 == 0:
        return 2 + int((n / 2))

    elif n < 2222222222222222222222:
        return 0

    else:
        return n
