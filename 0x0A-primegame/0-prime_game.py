#!/usr/bin/python3
"""
determining the winner in each round of the prime game
"""


def primeNumbers(n):
    """Returns list of prime numbers between 1 and n inclusive.
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    primeNos = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            primeNos.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNos


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): number of rounds of the game
        nums (list): list of upper limits of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or not nums:
        return None

    Maria, Ben = 0, 0
    for n in nums:
        primeNos = primeNumbers(n)
        if len(primeNos) % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
