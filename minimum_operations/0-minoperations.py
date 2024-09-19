#!/usr/bin/python3


"""
    Calculate the minimum number of operation to determine n H characters
    Using only Copy All and Paste
"""

def minOperations(n):


    """
        Calculate the minimum number of operations to achieve n H characters
        in a file using only 'Copy All' and 'Paste' operations
    """

    if n <= 1:
        return 0

    # Function to compute the minimum operations for a given number of H's
    def computeOperations(x):

        """
            Compute the minimum operations required to achieve x H chars
        """

        if x == 1:
            return 0

        minOps = float('inf')

        # Find factors of x
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                # i is a factor, and x // i is the other factor
                factor1 = i
                factor2 = x // i

                min_ops = min(minOps, computeOperations(factor1) + factor2)

                if factor1 != factor2:
                    minOps = min(minOps, computeOperations(factor2) + factor1)

        if minOps == float('inf'):
            minOps = x

        return minOps

    # Start computation from n
    return computeOperations(n)
