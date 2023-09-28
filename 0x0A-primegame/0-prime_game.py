#!/usr/bin/python3

"""
function to calculate winner of game of
prime numbers
"""


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a game
    based on prime number selection.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing
        the upper limits for each round.

    Returns:
        str or None: Name of the player with the most wins.
        Returns None if the winner cannot be determined.

    Raises:
        None.

    Example:

        >>> x = 3
        >>> nums = [4, 5, 1]
        >>> isWinner(x, nums)
        'Ben'
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        """Return a list of prime numbers up to n."""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        """Simulate a round of the game and return the winner."""
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    round_winners = [play_round(n) for n in nums]

    maria_wins = round_winners.count("Maria")
    ben_wins = round_winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
