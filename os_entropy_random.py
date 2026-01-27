import os


def random_from_os_entropy(num_bytes: int = 4) -> int:
    """
    Generate a random integer directly from OS entropy.

    Parameters
    ----------
    num_bytes : int
        Number of random bytes to read from OS

    Returns
    -------
    int
        Random integer generated from OS entropy
    """
    random_bytes = os.urandom(num_bytes)
    return int.from_bytes(random_bytes, byteorder="big")


# Example usage
value = random_from_os_entropy()
print("OS entropy random number:", value)
