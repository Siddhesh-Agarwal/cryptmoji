from cryptmoji import __version__, encrypt, decrypt


def test_version():
    assert __version__ == "2.1.0", "Version is not 2.1.0"


def test_1():
    assert "Hello, World!" == decrypt(encrypt("Hello, World!")), "Encryption and decryption do not work as expected"


def test_2():
    assert "Hello, World!" == decrypt(encrypt("Hello, World!", key="key"), key="key"), "Encryption and decryption do not work as expected"

if __name__ == "__main__":
    test_version()
    test_1()
    test_2()