from data import LENGTH, emojis


class Cryptmoji:
    def __init__(self, text: str, key: str = None):
        self.text = [i for i in text]
        self.key = key
        self.key_len = len(key) if key is not None else 0

    def encrypt(self) -> str:
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
        if self.key is not None:
            char_2_int = [
                ord(self.text[i]) + ord(self.key[i % self.key_len])
                for i in range(len(self.text))
            ]
        else:  # key is None
            char_2_int = [ord(self.text[i]) for i in range(len(self.text))]
        self.text = [emojis[i % LENGTH] for i in char_2_int]
        return "".join(self.text)

    def decrypt(self) -> str:
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
        emojis_2_int = [emojis.index(i) for i in self.text]
        if self.key is not None:
            decrypted = [
                emojis_2_int[i] - ord(self.key[i % len(self.key)])
                for i in range(len(emojis_2_int))
            ]
        else:
            decrypted = [emojis_2_int[i] for i in range(len(emojis_2_int))]
        self.text = [chr(i) for i in decrypted]
        return "".join(self.text)


if __name__ == "__main__":
    text = "Hello World!"
    key = "random_key"
    a = Cryptmoji(text, key)
    encrypted = a.encrypt()
    print(encrypted)
    print(a.decrypt())
