from constants import (
    alphabet, alphabet_length
)


def encrypt_vigenere(plaintext: str, key: str, reverse: bool = False) -> str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    key_len = len(key)
    key = key.lower()

    sign = [1, -1][reverse]

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
        shift = alphabet.index(key[char_i % key_len]) * sign
        new_alphabet_index = (char_alphabet_index + shift) % alphabet_length
        new_char = alphabet[new_alphabet_index]

        if char.isupper():
            plaintext[char_i] = new_char.upper()

        else:
            plaintext[char_i] = new_char

    plaintext = "".join(plaintext)
    return plaintext


def decrypt_vigenere(plaintext: str, key: str) -> str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """

    plaintext = encrypt_vigenere(plaintext, key, -1)
    return plaintext
