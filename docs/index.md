# 🐱‍👤 Cryptmoji

A simple emoji-based encryption-decryption library.

_______________________

## 📥 Installation

pip install the library:

```bash
pip install cryptmoji
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
