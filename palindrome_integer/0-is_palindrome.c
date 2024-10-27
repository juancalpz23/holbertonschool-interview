#include "palindrome.h"

/**
 * is_palindrome - Checks whether an unsigned integer is a palindrome.
 * @n: The unsigned long integer to be checked.
 *
 * Return: 1 if n is a palindrome, 0 otherwise.
 */
int is_palindrome(unsigned long n)
{
    unsigned long reversed = 0, original = n;

    /* Reverse the given number */
    while (n != 0)
    {
        reversed = reversed * 10 + (n % 10);
        n /= 10;
    }

    /* Compare the original number with the reversed one */
    return (original == reversed ? 1 : 0);
}
