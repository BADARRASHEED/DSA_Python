def factorial(num):
    """Calculate the factorial of a number using recursion.

    Args:
        num (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def sum_of_digits(num):
    """Calculate the sum of the digits of a number using recursion.

    Args:
        num (int): The number to calculate the sum of digits for.

    Returns:
        int: The sum of the digits.
    """
    if num == 0:
        return 0
    else:
        return num % 10 + sum_of_digits(num // 10)


def power(base, exponent):
    """Calculate the power of a number using recursion.

    Args:
        base (int): The base number.
        exponent (int): The exponent.

    Returns:
        int: The result of base raised to the power of exponent.
    """
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)


def gcd(a, b):
    """Calculate the greatest common divisor (GCD) of two numbers using recursion.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def reverse_string(s):
    """Reverse a string using recursion.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])


def count_occurrences(s, char):
    """Count occurrences of a character in a string using recursion.

    Args:
        s (str): The string to search.
        char (str): The character to count.
    Returns:
        int: The number of occurrences of the character in the string.
    """
    if len(s) == 0:
        return 0
    else:
        count = 1 if s[0] == char else 0
        return count + count_occurrences(s[1:], char)


# Example usage:
if __name__ == "__main__":
    print(factorial(5))  # Output: 120
    print(fibonacci(6))  # Output: 8
    print(sum_of_digits(1234))  # Output: 10
    print(power(2, 3))  # Output: 8
    print(gcd(48, 18))  # Output: 6
    print(reverse_string("hello"))  # Output: "olleh"
    print(count_occurrences("hello world", "o"))  # Output: 2
