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
from cryptmoji import Cryptmoji

text = "Hello World!"
key = "random_key" # makes the encryption stronger (optional)

a = Cryptmoji(text, key=key)
encrypted = a.encrypt()
# The encrypt and decrypt functions return the value
print(encrypted)
# 🎚️🎨🎼🎲🏀🍯🎓🎼🎹🏂🎸🍤

a.decrypt() 
# The encrypt and decrypt functions change the value in-place
print(decrypted)
# Hello World!
```
