from typing import Union
from cryptmoji.data import EMOJIS

LENGTH = len(EMOJIS)


def encrypt(text: str, *, key: Union[str, None] = None) -> str:
    """
    Encrypts a string to emojis.

    Args
    ----
    text: str
        The string to encrypt
    key: str
        The string to use for increasing complexity of encryption

    Returns
    -------
    encrypted: str
        The encrypted string
    """
    iterator = range(len(text))
    if key is None:
        char_2_int = [ord(text[i]) for i in iterator]
    else:  # key is not None
        char_2_int = [ord(text[i]) + ord(key[i % len(key)]) for i in iterator]
    char_arr = [EMOJIS[i % LENGTH] for i in char_2_int]
    return "".join(char_arr)


def decrypt(text: str, *, key: Union[str, None] = None) -> str:
    """
    Decrypts a string from emojis.

    Args
    ----
    text: str
        The string to decrypt
    key: str
        The string used encryption

    Returns
    -------
    encrypted: str
        The decrypted string
    """
    emojis_2_int = [EMOJIS.index(i) for i in text]
    iterator = range(len(emojis_2_int))
    if key is not None:
        decrypted = [emojis_2_int[i] - ord(key[i % len(key)]) for i in iterator]
    else:
        decrypted = [emojis_2_int[i] for i in iterator]
    char_arr = [chr(i) for i in decrypted]
    return "".join(char_arr)
