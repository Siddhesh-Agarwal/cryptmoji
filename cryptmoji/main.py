from cryptmoji.data import EMOJIS

LENGTH = len(EMOJIS)


def encrypt(text: str, key: str = None) -> str:
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
    if key is not None:
        char_2_int = [ord(text[i]) + ord(key[i % len(key)]) for i in range(len(text))]
    else:  # key is None
        char_2_int = [ord(text[i]) for i in range(len(text))]
    text = [EMOJIS[i % LENGTH] for i in char_2_int]
    return "".join(text)


def decrypt(text: str, key: str = None) -> str:
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
    if key is not None:
        decrypted = [
            emojis_2_int[i] - ord(key[i % len(key)]) for i in range(len(emojis_2_int))
        ]
    else:
        decrypted = [emojis_2_int[i] for i in range(len(emojis_2_int))]
    text = [chr(i) for i in decrypted]
    return "".join(text)
