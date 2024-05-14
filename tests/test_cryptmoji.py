from typing import Union
from cryptmoji import encrypt, decrypt


def test_general(text: str, key: Union[str, None] = None):
    return decrypt(encrypt(text, key=key), key=key) == text


def test_1():
    text = "Hello, World!"
    assert test_general(text), "Encryption and decryption do not work as expected"


def test_2():
    key = "test_key"
    text = "Hello, World!"
    assert test_general(
        text, key=key
    ), "Encryption and decryption do not work as expected"


def test_3():
    key = "53cr3t_k3y"
    text = "Hello, World!"
    assert test_general(
        text, key=key
    ), "Encryption and decryption do not work as expected"


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
