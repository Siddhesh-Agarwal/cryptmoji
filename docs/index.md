# 🐱‍👤 Cryptmoji

A simple emoji-based encryption-decryption library.

_______________________

## 📥 Installation

pip install the library:

```sh
pip install cryptmoji
```

_______________________

## 📝 Usage

```python
from cryptmoji import Cryptmoji

text = "Hello World!"
key = "random_key" # makes the encryption stronger (optional)

a = Cryptmoji(text, key=key)
# The encrypt and decrypt functions return the value
encrypted = a.encrypt()
print(encrypted)
# 🎚️🎨🎼🎲🏀🍯🎓🎼🎹🏂🎸🍤

# The encrypt and decrypt functions change the value in-place too
a.decrypt() 
print(decrypted)
# Hello World!
```

_______________________

## cryptmoji.Cryptmoji

### encrypt()

### decrypt()

_______________________

## cryptmoji.data

`cryptmoji.data` contains 2 variables i.e. `emojis` and `LENGTH`. 
1. `emojis` is a list of emojis that are possible `cryptmoji` to generate.
2. `LENGTH` is `len(emojis)`.
