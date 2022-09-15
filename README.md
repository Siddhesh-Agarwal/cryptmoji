# 🐱‍👤 Cryptmoji

A simple emoji-based encryption-decryption library.
_______________________

## 📥 Installation

pip install the library:

```sh
pip install cryptmoji
```

## 📝 Usage

```python
from cryptmoji import encrypt, decrypt

text = "Hello, world!"
key = "random_key" # makes the encryption stronger (optional)

# The encrypt and decrypt functions return the value
encrypted = encrypt(text, key)
print(encrypted)
# '🎽🏉🏭🏣🏴🎐🍵🐀🏧🐉🏴🏈🎆'

# The encrypt and decrypt functions change the value in-place too
decrypted = decrypt(encrypted, key)
print(decrypted)
# 'Hello, world!'
```
