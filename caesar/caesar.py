from constants import (
    alphabet, alphabet_length
)


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """

    if abs(shift) > alphabet_length:
        raise ValueError(
            f"Shift must be between -{alphabet_length} and {alphabet_length}"
            )

    plaintext = list(plaintext)

    for char_i in range(len(plaintext)):
        char = plaintext[char_i]

        if (
            char not in alphabet
        ) and (
            char.lower() not in alphabet
        ):
            continue

        tmp = char
        if char.isupper():
            tmp = char.lower()
        char_alphabet_index = alphabet.index(tmp)
        new_alphabet_index = (char_alphabet_index + shift) % alphabet_length
        new_char = alphabet[new_alphabet_index]

        if char.isupper():
            plaintext[char_i] = new_char.upper()

        else:
            plaintext[char_i] = new_char

    plaintext = "".join(plaintext)
    return plaintext


def decrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """

    plaintext = encrypt_caesar(plaintext, -shift)
    return plaintext
