from cryptmoji import __version__, encrypt, decrypt


def test_version():
    assert __version__ == "2.0.0"


def test_1():
    assert "Hello, World!" == decrypt(encrypt("Hello, World!"))


def test_2():
    assert "Hello, World!" != decrypt(encrypt("Hello, World!", "key"))


def test_3():
    assert "Hello, World!" == decrypt(encrypt("Hello, World!", "key"), "key")
