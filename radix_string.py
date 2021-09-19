import string


def radix_string(number: int, radix: int) -> str:
    """Convert integer to radix string

    Args:
        number (int): a number to convert
        radix (int): a bast convert to

    Raises:
        TypeError: number must be int
        TypeError: radix must be int
        ValueError: radix must be more than 2

    Returns:
        str: a radix string
    """
    if not isinstance(number, int):
        raise TypeError("number must be int")
    if not isinstance(radix, int):
        raise TypeError("radix must be int")
    if radix < 2:
        raise ValueError("radix must be more than 2")

    basic_alphabet = string.digits + string.ascii_lowercase

    result = ""

    if number < 0:
        number = -number
        sign = "-"
    else:
        sign = ""

    while True:
        number, rdigit = divmod(number, radix)
        letter = (
            f"[{rdigit}]" if rdigit >= len(basic_alphabet) else basic_alphabet[rdigit]
        )
        result = letter + result
        if number == 0:
            return sign + result
