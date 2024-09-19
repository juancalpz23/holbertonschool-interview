#!/usr/bin/python3
"""
Calculate the minimum number of operation to determine n H characters
Using only Copy All and Paste
"""

def minOperations(n):

    """
    Calculate the minimum number of operations to achieve exactly n 'H' characters
    in a file using only 'Copy All' and 'Paste' operations
    """

    if n <= 1:
        return 0

    # Function to compute the minimum operations for a given number of H's
    def compute_operations(x):
        """
        Compute the minimum operations required to achieve x 'H' characters.
        """

        if x == 1:
            return 0
        
        min_ops = float('inf')
        
        # Find factors of x
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                # i is a factor, and x // i is the other factor
                factor1 = i
                factor2 = x // i
                min_ops = min(min_ops, compute_operations(factor1) + factor2)
                if factor1 != factor2:
                    min_ops = min(min_ops, compute_operations(factor2) + factor1)
        
        return min_ops
    
    # Start computation from n
    return compute_operations(n)