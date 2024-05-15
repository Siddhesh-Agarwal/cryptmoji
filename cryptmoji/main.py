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
    if key:
        key_len = len(key)
        iterator = range(len(text))
        char_2_int = map(lambda x: ord(text[x]) + ord(key[x % key_len]), iterator)
    else:
        char_2_int = map(ord, text)
    return "".join(map(lambda x: EMOJIS[x % LENGTH], char_2_int))


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
    if key:
        key_len = len(key)
        decrypted = map(
            lambda x: (emojis_2_int[x] - ord(key[x % key_len]) + LENGTH) % LENGTH,
            iterator,
        )
    else:
        decrypted = map(lambda x: emojis_2_int[x], iterator)
    return "".join(map(chr, decrypted))
