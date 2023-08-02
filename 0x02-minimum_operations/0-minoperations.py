#!/bin/python3
"""
	An interview challenge
"""


def minOperations(n):
    """
    A function which returns the fewest operations needed to get 'n' occurrences of H in a file using copy & paste operations.

    Args:
        n (int): Number of H required in the file

    Returns:
        int: Minimum number of operations needed
    """
    operations = 0  # Keeps track of the copy & paste operations made
    totalN = 1  # Represents the current total n of H in the file

    if n <= 1:
        return 0

    while totalN != n:
        if totalN < n:
            if n % totalN == 0:  # If 'n' is divisible by current totalN, we can double it
                totalN *= 2
            else:  # Otherwise, we need to add one 'H'
                totalN += 1
            operations += 1

        if totalN > n:
            totalN -= 1
            operations += 1

    return operations
print(minOperations(9))
