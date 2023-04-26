# 🥷 Cryptmoji

A simple emoji-based encryption-decryption library.

![Downloads](https://static.pepy.tech/personalized-badge/cryptmoji?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)
_______________________

## 📥 Installation

pip install the library:

```sh
pip install cryptmoji
```

Check the [Documentation](https://siddhesh-agarwal.github.io/cryptmoji/)

## 📝 Usage

```python
from cryptmoji import encrypt, decrypt

text = "Hello, world!"
key = "random_key" # makes the encryption stronger (optional)

# The encrypt and decrypt functions return the value
decrypted = decrypt(encrypted, key=key)
print(decrypted)
# '🎽🏉🏭🏣🏴🎐🍵🐀🏧🐉🏴🏈🎆'

# The encrypt and decrypt functions change the value in-place too
decrypted = decrypt(encrypted, key=key)
print(decrypted)
# 'Hello, world!'
```

