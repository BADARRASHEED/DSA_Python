import secrets


def secure_random_int(min_value: int, max_value: int) -> int:
    """
    Generate a cryptographically secure random integer
    using OS entropy.

    Parameters
    ----------
    min_value : int
        Lower bound (inclusive)
    max_value : int
        Upper bound (inclusive)

    Returns
    -------
    int
        Secure random integer between min_value and max_value
    """
    return secrets.randbelow(max_value - min_value + 1) + min_value


# Example usage
number = secure_random_int(1, 100)
print("Secure random number:", number)
