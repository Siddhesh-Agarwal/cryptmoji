# 🥷🏾 Cryptmoji

A simple emoji-based encryption-decryption library.

_______________________

## 📥 Installation

You can use the [pip](https://pypi.org/project/pip/) package manager to install the library.

```sh
pip install cryptmoji
```

or use [poetry](https://python-poetry.org/):

```sh
poetry add cryptmoji
```

_______________________

## 📝 Usage

```python
from cryptmoji import encrypt, decrypt

text = "Hello, world!"
key = "random_key" # makes the encryption stronger (optional)

# The encrypt and decrypt functions return the value
encrypted = encrypt(text, key=key)
print(encrypted)
# '🎽🏉🏭🏣🏴🎐🍵🐀🏧🐉🏴🏈🎆'

# The encrypt and decrypt functions change the value in-place too
decrypted = decrypt(encrypted, key=key)
print(decrypted)
# 'Hello, world!'
```

_______________________

## cryptmoji

### encrypt()

Encryption can be done like this (without a key):

```python
from cryptmoji import encrypt

text = "Hello, world!"
encrypted = encrypt(text)
print(encrypted)
# 🌾🍛🍢🍢🍥🌕🌉🍭🍥🍨🍢🍚🌊
```

or like this (with a key):

```python
from cryptmoji import encrypt

text = "Hello, world!"
key = "random_key"
encrypted = encrypt(text, key=key)
print(encrypted)
# 🎽🏉🏭🏣🏴🎐🍵🐀🏧🐉🏴🏈🎆
```

### decrypt()

Decryption can be done like this (without a key):

```python
from cryptmoji import decrypt

text = "🌾🍛🍢🍢🍥🌕🌉🍭🍥🍨🍢🍚🌊"
decrypted = decrypt(encrypted)
print(decrypted)
# Hello, world!
```

or like this (with a key):

```python
from cryptmoji import decrypt

text = "🎽🏉🏭🏣🏴🎐🍵🐀🏧🐉🏴🏈🎆"
key = "random_key"
decrypted = decrypt(encrypted, key=key)
print(decrypted)
# Hello, world!
```

_______________________

## Command line tool

### Installation

```sh
pip install cryptmoji[cli]
```

### Usage

To encrypt:

```sh
$ cryptmoji encrypt "Hello World"
Key (optional):
🌾🍛🍢🍢🍥🌕🌉🍭🍥🍨🍢🍚🌊
```

To decrypt:

```sh
$ cryptmoji decrypt "🌾🍛🍢🍢🍥🌕🌉🍭🍥🍨🍢🍚🌊"
Key (optional):
Hello World
```