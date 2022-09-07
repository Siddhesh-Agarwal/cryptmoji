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

This is a class and its constructor is as follows:

```python
__init__(self, text: str, key: str = None)
```

The class constructor takes in a compulsory parameter i.e. the text to encrypt/decrypt. It also takes in an optional parameter (i.e. `key`) to increase the complexity of the encryption.

```
from cryptmoji import Cryptmoji

tool = Cryptmoji(temp)
```

### encrypt()

Encryption can be done using:

```python
tool.encrypt()
print(tool)
```

apart from inplace encryption, the values are also returned.

```python
encrypted = tool.decrypt()
print(encrypted)
```

### decrypt()

Decryption can be done using:

```python
tool.decrypt()
print(tool)
```

apart from inplace decryption, the values are also returned.

```python
decrypted = tool.decrypt()
print(decrypted)
```

